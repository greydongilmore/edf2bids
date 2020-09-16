
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 13:49:51 2018

@author: Greydon
"""
import os
import numpy as np
import pandas as pd
pd.set_option('precision', 6)
import datetime
import shutil
from PySide2 import QtCore
import time
import re
import io


from edflibpy import EDFreader
from helpers import EDFReader, bidsHelper, fix_sessions, sec2time, deidentify_edf

class WorkerKilledException(Exception):
	pass

class WorkerSignals(QtCore.QObject):
	'''
	Defines the signals available from a running worker thread.

	Supported signals are:

	finished
		No data
	
	error
		`tuple` (exctype, value, traceback.format_exc() )
	
	result
		`object` data returned from processing, anything

	progress
		`int` indicating % progress 

	'''
	finished = QtCore.Signal()
	progressEvent = QtCore.Signal(str)
	
class edf2bids(QtCore.QRunnable):
	"""
	This class is a thread, which manages one thread of control within the GUI.
	
	:param new_sessions: Dictionary containing information about each subject. Wether there are new sessions to process in the input directory. 
	:type new_sessions: dictionary
	:param file_info: Information about each subject file in the input directory
	:type file_info: dictionary
	:param input_path: Path to the input directory.
	:type input_path: string
	:param output_path: path to the output directory
	:type output_path: string
	:param coordinates: Optional list of electrode coordinates (x,y,z)
	:type coordinates: list or None
	:param make_dir: Make the directory
	:type make_dir: boolean
	:param overwrite: If duplicate data is present in the output directory overwrite it.
	:type overwrite: boolean
	:param verbose: Print out process steps.
	:type verbose: boolean
	:param annotation_extract: Extract annotations from the edf file.
	:type annotation_extract: boolean
	:param compress: Compress the edf file
	:type compress: boolean
	
	"""
	
	def __init__(self):	
		super(edf2bids, self).__init__()
		
		self.new_sessions = []
		self.file_info = []
		self.chan_label_file = []
		self.input_path = []
		self.output_path = []
		self.script_path = []
		self.coordinates = []
		self.make_dir = []
		self.overwrite = []
		self.verbose = []
		self.deidentify_source = []
		self.offset_date = []
		self.bids_settings = []
		self.test_conversion = []
		self.annotations_only = []
		
		self.signals = WorkerSignals()
		
		self.running = False
		self.userAbort = False
		self.is_killed = False
		
	def stop(self):
		self.running = False
		self.userAbort = True
	
	def kill(self):
		self.is_killed = True
	
	def write_annotations(self, data, data_fname, deidentify=True):
		self._annotations_data(data, data_fname, deidentify)
	
	def overwrite_annotations(self, events, data_fname, identity_idx, tal_indx, strings, action):
		
		for ident in identity_idx:
			block_chk = events[ident][-1]
			assert(block_chk>=0)
			
			with open(data_fname, 'rb') as fid:
				assert(fid.tell() == 0)
				fid.seek((block_chk-(self.header['chan_info']['n_samps'][tal_indx]*2)), io.SEEK_SET)
				cnv_buf=bytearray(self.header['chan_info']['n_samps'][tal_indx]*2)
				fid.readinto(cnv_buf)
					
			if isinstance(strings, dict):
				replace_idx = [i for i,x in enumerate(strings.keys()) if x.lower() in events[ident][2].lower()]
			else:
				replace_idx = [i for i,x in enumerate(strings) if x.lower() in events[ident][2].lower()]
			
			new_block=[]
			for irep in replace_idx:
				if action == 'replaceExact':
					if new_block:
						new_block = bytearray(re.sub(bytes(strings[irep],'latin-1').lower(),bytes(''.join(np.repeat('X', len(strings[irep]))),'latin-1'),new_block.lower()))
						events[ident][2] = re.sub(strings[irep].lower(),''.join(np.repeat('X', len(strings[irep]))),events[ident][2].lower())
					else:
						new_block = bytearray(re.sub(bytes(strings[irep],'latin-1').lower(),bytes(''.join(np.repeat('X', len(strings[irep]))),'latin-1'),cnv_buf.lower()))
						events[ident][2] = re.sub(strings[irep].lower(),''.join(np.repeat('X', len(strings[irep]))),events[ident][2].lower())
					
					assert(len(new_block)==len(cnv_buf))
				
				elif action == 'replaceMatch':
					replace_string = list(strings.values())[irep]
					new_block = cnv_buf.replace(bytes(events[ident][2],'latin-1'),bytes(replace_string,'latin-1'))
					events[ident][2] = replace_string
					new_block = new_block+bytes('\x00'*(len(cnv_buf)-len(new_block)),'latin-1')
					
					assert(len(new_block)==len(cnv_buf))
					
			if new_block:
				with open(data_fname, 'r+b') as fid:
					assert(fid.tell() == 0)
					fid.seek((block_chk-(self.header['chan_info']['n_samps'][tal_indx]*2)), io.SEEK_SET)
					if fid.tell()==(block_chk-(self.header['chan_info']['n_samps'][tal_indx]*2)):
						fid.write(new_block)
		
		return events
	
	def _annotations_data(self, file_info_run, data_fname, callback, deidentify):
		"""
		Constructs an annotations data tsv file about patient specific events from edf file.
		
		:param file_info_run: File header information for specific recording.
		:type file_info_run: dictionary
		:param annotation_fname: Filename for the annotations tsv file.
		:type annotation_fname: string
		:param data_fname: Path to the raw data file for specific recording.
		:type data_fname: string
		:param overwrite: If duplicate data is present in the output directory overwrite it.
		:type overwrite: boolean
		:param verbose: Print out process steps.
		:type verbose: boolean
		
		"""
		self.fname=data_fname
		
		file_in = EDFReader()
		file_in.open(data_fname)
		self.header = file_in.readHeader()
		
		overwrite_exact = [self.header['meas_info']['firstname'], self.header['meas_info']['lastname']]
# 		overwrite_exact = [header['meas_info']['firstname'], header['meas_info']['lastname']]
		overwrite_exact = [x for x in overwrite_exact if x is not None]
		overwrite_match={
						'montage': 'Montage Event'
						}
		remove_strings = []
	
		tal_indx = [i for i,x in enumerate(self.header['chan_info']['ch_names']) if x.endswith('Annotations')][0]
# 		tal_indx = [i for i,x in enumerate(header['chan_info']['ch_names']) if x.endswith('Annotations')][0]
		
		callback.emit('...')
		
		hdl=EDFreader(data_fname)
		events=hdl.annotationslist
		events=[list(x) for x in events]
		
		if deidentify:
			if overwrite_exact:
				### Replace any identifier strings
				identity_idx = [i for i,x in enumerate(events) if any(substring.lower() in x[2].lower() for substring in overwrite_exact) and 'montage' not in x[2].lower()]
				if identity_idx:
					events = self.overwrite_annotations(events, data_fname, identity_idx, tal_indx, overwrite_exact, 'replaceExact')
			
			if overwrite_match:
				identity_idx = [i for i,x in enumerate(events) if any(substring.lower() in x[2].lower() for substring in overwrite_match.keys()) and not any(substring.lower() == x[2].lower() for substring in list(overwrite_match.values()))]
				if identity_idx:
					events = self.overwrite_annotations(events, data_fname, identity_idx, tal_indx, overwrite_match, 'replaceMatch')
		
			if remove_strings:
				### Remove unwanted annoations
				identity_idx = [i for i,x in enumerate(events) if any(substring.lower() == x[2].lower() for substring in remove_strings)]
				if identity_idx:
					events = self.overwrite_annotations(events, data_fname, identity_idx, tal_indx, remove_strings, 'remove')
		
		annotation_data = pd.DataFrame({})
		if events:
			fulldate = datetime.datetime.strptime(self.header['meas_info']['meas_date'], '%Y-%m-%d %H:%M:%S')
			for iannot in events:
				data_temp = {'onset': iannot[0]/10000000,
							 'duration': iannot[1],
							 'time_abs': (fulldate + datetime.timedelta(seconds=(iannot[0]/10000000)+float(self.header['meas_info']['millisecond']))).strftime('%H:%M:%S.%f'),
							 'time_rel': sec2time(iannot[0]/10000000, 6),
							 'event': iannot[2]}
				annotation_data = pd.concat([annotation_data, pd.DataFrame([data_temp])], axis = 0)
			
		annotation_data.to_csv(self.annotation_fname, sep='\t', index=False, na_rep='n/a', line_terminator="", float_format='%.3f')
	
# 	def copyLargeFile(self, src: str, dest: str, callback):
# 		total_size = os.path.getsize(src)
# 		update_cnt = int(total_size/10)
# 		try:
# 			# check for optimisation opportunity
# 			if "b" in open(src).mode and "b" in open(dest).mode and open(src).readinto:
# 				return self._copyfileobj_readinto(src, dest, callback)
# 		except AttributeError:
# 			# one or both file objects do not support a .mode or .readinto attribute
# 			pass
# 	
# 		length = 1024 * 1024
# 		
# 		with open(src, 'rb') as fsrc:
# 			with open(dest, 'wb') as fdest:
# 				fsrc_read = fsrc.read
# 				fdst_write = fdest.write
# 			
# 				copied = 0
# 				while True:
# 					if self.is_killed:
# 						self.running = False
# 						raise WorkerKilledException
# 					else:
# 						buf = fsrc_read(length)
# 						if not buf:
# 							break
# 						fdst_write(buf)
# 						copied += len(buf)
# 						if update_cnt < copied:
# 							if update_cnt == int(total_size/10):
# 								callback.emit('copy{}%'.format(int(np.ceil((update_cnt/total_size)*100))))
# 							elif copied < (total_size-(int((total_size)/20))):
# 								callback.emit('{}%'.format(int(np.ceil((update_cnt/total_size)*100))))
# 							update_cnt += int(total_size/10)
# 				
# 				callback.emit('100%')
# 	
# 	def _copyfileobj_readinto(self, src: str, dest: str, callback):
# 		"""readinto()/memoryview() based variant of copyfileobj().
# 		*fsrc* must support readinto() method and both files must be
# 		open in binary mode.
# 		"""
# 		total_size = os.path.getsize(src)
# 		update_cnt = int(total_size/10)
# 		
# 		with open(src, 'rb') as fsrc:
# 			with open(dest, 'wb') as fdst:
# 				fsrc_readinto = fsrc.readinto
# 				fdst_write = fdst.write
# 			
# 				try:
# 					file_size = os.stat(fsrc.fileno()).st_size
# 				except OSError:
# 					file_size = 1024 * 1024
# 				length = min(file_size, 1024 * 1024)
# 			
# 				copied = 0
# 				with memoryview(bytearray(length)) as mv:
# 					while True:
# 						if self.is_killed:
# 							self.running = False
# 							raise WorkerKilledException
# 						else:
# 							n = fsrc_readinto(mv)
# 							if not n:
# 								break
# 							elif n < length:
# 								with mv[:n] as smv:
# 									fdst.write(smv)
# 							else:
# 								fdst_write(mv)
# 							copied += n
# 							if update_cnt < copied:
# 								if update_cnt == int(total_size/10):
# 									callback.emit('copy{}%'.format(int(np.ceil((update_cnt/total_size)*100))))
# 								elif copied < (total_size-(int((total_size)/20))):
# 									callback.emit('{}%'.format(int(np.ceil((update_cnt/total_size)*100))))
# 								update_cnt += int(total_size/10)
# 					
# 					callback.emit('100%')
				
	def copyLargeFile(self, src, dest, callback, buffer_size=16*1024):
		total_size = os.path.getsize(src)
		update_cnt = int(total_size/10)
		with open(src, 'rb') as fsrc:
			with open(dest, 'wb') as fdest:
				copied = 0
				while 1:
					if self.is_killed:
						self.running = False
						raise WorkerKilledException
					else:
						buf = fsrc.read(buffer_size)
						if not buf:
							break
						fdest.write(buf)
						copied += len(buf)
						if update_cnt < copied:
							if update_cnt == int(total_size/10):
								callback.emit('copy{}%'.format(int(np.ceil((update_cnt/total_size)*100))))
							elif copied < (total_size-(int((total_size)/20))):
								callback.emit('{}%'.format(int(np.ceil((update_cnt/total_size)*100))))
							update_cnt += int(total_size/10)

				callback.emit('100%')
	
	@QtCore.Slot()
	def run(self):
		"""
		Main loop for building BIDS database.
				
		"""
		if not self.userAbort:
			self.running = True
		
		participants_fname = bidsHelper(output_path=self.output_path).write_participants(return_fname=True)
		if os.path.exists(participants_fname):
			self.participant_tsv = pd.read_csv(participants_fname, sep='\t')
			
		try:
			for isub, values in self.new_sessions.items():
				subject_dir = self.file_info[isub][0][0]['SubDir']
				raw_file_path = os.path.join(self.input_path, subject_dir)
				
				if self.is_killed:
					self.running = False
					raise WorkerKilledException
					
				if values['newSessions']:
					sessions_fix = [x for x in values['session_changes'] if x[0] != x[1]]
					if sessions_fix:
						fix_sessions(sessions_fix, values['num_sessions'], self.output_path, isub)
					
					for ises in range(len(values['session_labels'])):
						file_data = self.file_info[isub][ises]
						session_id = values['session_labels'][ises].split('-')[-1]
						
						if 'Scalp' in file_data[0]['RecordingType']:
							kind = 'eeg'
						elif 'iEEG' in file_data[0]['RecordingType']:
							kind = 'ieeg'
						
						self.conversionStatusText = '\nStarting conversion: session {} of {} for {} at {}'.format(str(ises+1), str(len(values['session_labels'])), isub, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
						self.signals.progressEvent.emit(self.conversionStatusText)
						
						bids_helper = bidsHelper(subject_id=isub, session_id=session_id, kind='ieeg', output_path=self.output_path, bids_settings=self.bids_settings, make_sub_dir=True)
						
						num_runs = len(file_data)
						
						for irun in range(num_runs):
							if 'Full' in file_data[irun]['RecordingLength']:
								task_id = 'full'
							elif 'Clip' in file_data[irun]['RecordingLength']:
								task_id = 'clip'
							elif 'CS' in file_data[irun]['RecordingLength']:
								task_id = 'stim'
							
							if 'Ret' in file_data[irun]['Retro_Pro']:
								task_id = task_id + 'ret'
								
							run_num = str(irun+1).zfill(2)
							
							bids_helper.task_id=task_id
							bids_helper.run_num=run_num
							
							data_fname = bids_helper.make_bids_filename(suffix = kind + '.edf')
							
							if not self.test_conversion:
								source_name = os.path.join(raw_file_path, file_data[irun]['FileName'])
								self.annotation_fname = bids_helper.make_bids_filename(suffix='annotations.tsv')
								if not self.annotations_only:
									if self.deidentify_source:
										source_name, epochLength = deidentify_edf(source_name, isub, self.offset_date, True)
										self.bids_settings['json_metadata']['EpochLength'] = epochLength
										
									self.copyLargeFile(source_name, data_fname, self.signals.progressEvent)
									
									if not self.deidentify_source:
										temp_name, epochLength = deidentify_edf(data_fname, isub, self.offset_date, False)
										self.bids_settings['json_metadata']['EpochLength'] = epochLength
									
									self.write_annotations(file_data[irun], data_fname, self.signals.progressEvent, deidentify=True)
									
									if file_data[irun]['chan_label']:
										file_in = EDFReader()
										file_in.open(data_fname)
										chan_label_file=file_in.chnames_update(os.path.join(raw_file_path, file_data[irun]['chan_label'][0]), self.bids_settings, write=True)
									elif file_data[irun]['ses_chan_label']:
										file_in = EDFReader()
										file_in.open(data_fname)
										chan_label_file=file_in.chnames_update(os.path.join(raw_file_path, file_data[irun]['ses_chan_label'][0]), self.bids_settings, write=True)
								else:
									self.write_annotations(file_data[irun], source_name, self.signals.progressEvent, deidentify=False)
							
							else:
								if self.deidentify_source:
									source_name = os.path.join(raw_file_path, file_data[irun]['FileName'])
									source_name, epochLength = deidentify_edf(source_name, isub, self.offset_date, True)
									self.bids_settings['json_metadata']['EpochLength'] = epochLength
								else:
									self.bids_settings['json_metadata']['EpochLength'] = 0
							
							scan_fname=data_fname.split(isub+os.path.sep)[-1].replace(os.path.sep,'/')
							bids_helper.write_scans(scan_fname, file_data[irun], self.offset_date)
							
							bids_helper.write_channels(file_data[irun])
							bids_helper.write_sidecar(file_data[irun])
						
						bids_helper.write_electrodes(file_data[0], coordinates=None)
						
						code_output_path = os.path.join(self.output_path, 'code', 'edf2bids')
						code_path = bids_helper.make_bids_folders(path_override=code_output_path, make_dir=True)
						
						shutil.copy(os.path.join(self.script_path, 'edf2bids.py'), code_path)
						shutil.copy(os.path.join(self.script_path, 'helpers.py'), code_path)
					
						self.conversionStatusText = 'Finished conversion: session {} of {} for {} at {}'.format(str(ises+1), str(len(values['session_labels'])), isub, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
						self.signals.progressEvent.emit(self.conversionStatusText)
					
					time.sleep(0.1)
					
					if isub not in list(self.participant_tsv['participant_id']):
						bids_helper.write_participants(self.file_info[isub][0])
						self.participant_tsv = pd.read_csv(participants_fname, sep='\t')
				else:
					self.conversionStatusText = 'Participant {} already exists in the dataset! \n'.format(isub)
					self.signals.progressEvent.emit(self.conversionStatusText)
			
		except WorkerKilledException:
			self.running = False
			pass
		
		finally:
			self.running = False
			self.signals.finished.emit()





