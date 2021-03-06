# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_layout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1607, 979)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"eplink_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionLoad_data = QAction(MainWindow)
        self.actionLoad_data.setObjectName(u"actionLoad_data")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.actionLoad_data.setFont(font1)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setFont(font1)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionSettings.setFont(font1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setMinimumSize(QSize(0, 600))
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(4)
        self.splitter.setChildrenCollapsible(False)
        self.widget_6 = QWidget(self.splitter)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.widget_6)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_4 = QWidget(self.widget_6)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy3)
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.loadDirButton = QPushButton(self.widget_4)
        self.loadDirButton.setObjectName(u"loadDirButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.loadDirButton.sizePolicy().hasHeightForWidth())
        self.loadDirButton.setSizePolicy(sizePolicy4)
        self.loadDirButton.setMinimumSize(QSize(175, 30))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        self.loadDirButton.setFont(font2)
        self.loadDirButton.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.loadDirButton)

        self.verticalSpacer = QSpacerItem(20, 226, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget_4)

        self.treeViewLoad = QTreeWidget(self.widget_6)
        self.treeViewLoad.setObjectName(u"treeViewLoad")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(200)
        sizePolicy5.setHeightForWidth(self.treeViewLoad.sizePolicy().hasHeightForWidth())
        self.treeViewLoad.setSizePolicy(sizePolicy5)
        self.treeViewLoad.setMinimumSize(QSize(0, 0))
        self.treeViewLoad.setMaximumSize(QSize(16777215, 16777215))
        self.treeViewLoad.setFont(font1)
        self.treeViewLoad.setContextMenuPolicy(Qt.PreventContextMenu)
        self.treeViewLoad.setAcceptDrops(True)
        self.treeViewLoad.setAutoFillBackground(True)
        self.treeViewLoad.setFrameShape(QFrame.Box)
        self.treeViewLoad.setFrameShadow(QFrame.Sunken)
        self.treeViewLoad.setLineWidth(1)
        self.treeViewLoad.setMidLineWidth(1)
        self.treeViewLoad.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeViewLoad.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.treeViewLoad.setAlternatingRowColors(True)
        self.treeViewLoad.setSelectionMode(QAbstractItemView.NoSelection)
        self.treeViewLoad.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.treeViewLoad.setAnimated(False)
        self.treeViewLoad.setColumnCount(0)
        self.treeViewLoad.header().setVisible(True)
        self.treeViewLoad.header().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.treeViewLoad)

        self.splitter.addWidget(self.widget_6)
        self.widget_8 = QWidget(self.splitter)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_5 = QWidget(self.widget_8)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.outDirButton = QPushButton(self.widget_5)
        self.outDirButton.setObjectName(u"outDirButton")
        sizePolicy4.setHeightForWidth(self.outDirButton.sizePolicy().hasHeightForWidth())
        self.outDirButton.setSizePolicy(sizePolicy4)
        self.outDirButton.setMinimumSize(QSize(175, 30))
        self.outDirButton.setFont(font2)
        self.outDirButton.setLayoutDirection(Qt.LeftToRight)
        self.outDirButton.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.outDirButton)

        self.sText = QLabel(self.widget_5)
        self.sText.setObjectName(u"sText")
        self.sText.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sText.sizePolicy().hasHeightForWidth())
        self.sText.setSizePolicy(sizePolicy6)
        self.sText.setMinimumSize(QSize(175, 0))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.sText.setFont(font3)
        self.sText.setAlignment(Qt.AlignCenter)
        self.sText.setWordWrap(True)

        self.verticalLayout.addWidget(self.sText)

        self.verticalSpacer_2 = QSpacerItem(20, 211, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.treeViewOutput = QTreeWidget(self.widget_8)
        self.treeViewOutput.setObjectName(u"treeViewOutput")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(200)
        sizePolicy7.setHeightForWidth(self.treeViewOutput.sizePolicy().hasHeightForWidth())
        self.treeViewOutput.setSizePolicy(sizePolicy7)
        self.treeViewOutput.setMinimumSize(QSize(0, 0))
        self.treeViewOutput.setFont(font1)
        self.treeViewOutput.setContextMenuPolicy(Qt.PreventContextMenu)
        self.treeViewOutput.setAcceptDrops(True)
        self.treeViewOutput.setAutoFillBackground(True)
        self.treeViewOutput.setFrameShape(QFrame.Box)
        self.treeViewOutput.setFrameShadow(QFrame.Sunken)
        self.treeViewOutput.setLineWidth(1)
        self.treeViewOutput.setMidLineWidth(1)
        self.treeViewOutput.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeViewOutput.setAlternatingRowColors(True)
        self.treeViewOutput.setSelectionMode(QAbstractItemView.NoSelection)
        self.treeViewOutput.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.treeViewOutput.setColumnCount(0)
        self.treeViewOutput.header().setVisible(True)
        self.treeViewOutput.header().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.treeViewOutput)

        self.splitter.addWidget(self.widget_8)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.splitter)

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 300))
        self.gridLayout = QGridLayout(self.widget_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.widget_7)
        self.groupBox.setObjectName(u"groupBox")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.groupBox.setFont(font4)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.deidentifyInputDir = QCheckBox(self.groupBox)
        self.deidentifyInputDir.setObjectName(u"deidentifyInputDir")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.deidentifyInputDir.setFont(font5)

        self.verticalLayout_4.addWidget(self.deidentifyInputDir)

        self.offsetDate = QCheckBox(self.groupBox)
        self.offsetDate.setObjectName(u"offsetDate")
        self.offsetDate.setFont(font5)
        self.offsetDate.setChecked(True)

        self.verticalLayout_4.addWidget(self.offsetDate)

        self.dryRun = QCheckBox(self.groupBox)
        self.dryRun.setObjectName(u"dryRun")
        self.dryRun.setFont(font5)

        self.verticalLayout_4.addWidget(self.dryRun)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.widget_7)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 150))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(self.widget)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy8)
        self.cancelButton.setMinimumSize(QSize(150, 0))
        self.cancelButton.setMaximumSize(QSize(150, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.cancelButton.setPalette(palette)
        self.cancelButton.setFont(font4)
        self.cancelButton.setStyleSheet(u"background-color: rgb(255,0,0);\n"
"color: black")
        self.cancelButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.cancelButton)

        self.convertButton = QPushButton(self.widget)
        self.convertButton.setObjectName(u"convertButton")
        sizePolicy8.setHeightForWidth(self.convertButton.sizePolicy().hasHeightForWidth())
        self.convertButton.setSizePolicy(sizePolicy8)
        self.convertButton.setMinimumSize(QSize(150, 0))
        self.convertButton.setMaximumSize(QSize(150, 16777215))
        self.convertButton.setFont(font2)
        self.convertButton.setStyleSheet(u"background-color: rgb(79, 232, 109);\n"
"color: black")

        self.horizontalLayout_2.addWidget(self.convertButton)

        self.spredButton = QPushButton(self.widget)
        self.spredButton.setObjectName(u"spredButton")
        sizePolicy8.setHeightForWidth(self.spredButton.sizePolicy().hasHeightForWidth())
        self.spredButton.setSizePolicy(sizePolicy8)
        self.spredButton.setMinimumSize(QSize(150, 0))
        self.spredButton.setMaximumSize(QSize(150, 16777215))
        self.spredButton.setFont(font4)
        self.spredButton.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: black")

        self.horizontalLayout_2.addWidget(self.spredButton)

        self.imagingButton = QPushButton(self.widget)
        self.imagingButton.setObjectName(u"imagingButton")
        sizePolicy8.setHeightForWidth(self.imagingButton.sizePolicy().hasHeightForWidth())
        self.imagingButton.setSizePolicy(sizePolicy8)
        self.imagingButton.setMinimumSize(QSize(150, 0))
        self.imagingButton.setMaximumSize(QSize(150, 16777215))
        self.imagingButton.setFont(font4)
        self.imagingButton.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: black")

        self.horizontalLayout_2.addWidget(self.imagingButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.widget)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)

        self.verticalLayout_3.addWidget(self.label)

        self.conversionStatus = QPlainTextEdit(self.widget_3)
        self.conversionStatus.setObjectName(u"conversionStatus")
        self.conversionStatus.setMinimumSize(QSize(0, 200))
        self.conversionStatus.setMaximumSize(QSize(16777215, 300))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(9)
        self.conversionStatus.setFont(font6)
        self.conversionStatus.setFrameShape(QFrame.Box)
        self.conversionStatus.setMidLineWidth(1)
        self.conversionStatus.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_3.addWidget(self.conversionStatus)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.widget_3)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font7 = QFont()
        font7.setFamily(u"Arial")
        self.statusbar.setFont(font7)
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1607, 20))
        self.menuBar.setFont(font1)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font1)
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad_data)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        self.actionLoad_data.triggered.connect(self.loadDirButton.showMenu)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"edf2bids converter", None))
        self.actionLoad_data.setText(QCoreApplication.translate("MainWindow", u"Load data", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.loadDirButton.setText(QCoreApplication.translate("MainWindow", u"Input Directory", None))
        self.outDirButton.setText(QCoreApplication.translate("MainWindow", u"Output Directory", None))
        self.sText.setText(QCoreApplication.translate("MainWindow", u"Checked items are already in output directory.", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Settings Panel", None))
        self.deidentifyInputDir.setText(QCoreApplication.translate("MainWindow", u"De-identify input directory", None))
        self.offsetDate.setText(QCoreApplication.translate("MainWindow", u"Offset dates", None))
        self.dryRun.setText(QCoreApplication.translate("MainWindow", u"Dry run (no EDF)", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.spredButton.setText(QCoreApplication.translate("MainWindow", u"SPReD", None))
        self.imagingButton.setText(QCoreApplication.translate("MainWindow", u"Imaging", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Conversion Status", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

