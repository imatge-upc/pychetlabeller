# Form implementation generated from reading ui file 'labeller.ui'
#
# Created: Mon Nov  2 13:15:18 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import  QtCore, QtGui, QtWidgets


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1211, 872)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.dockWidget = QtWidgets.QDockWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.autosave_chk = QtWidgets.QCheckBox(self.dockWidgetContents_2)
        self.autosave_chk.setChecked(False)
        self.autosave_chk.setObjectName(_fromUtf8("autosave_chk"))
        self.gridLayout_4.addWidget(self.autosave_chk, 4, 0, 1, 1)
        self.label_folder_btn = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.label_folder_btn.setObjectName(_fromUtf8("label_folder_btn"))
        self.gridLayout_4.addWidget(self.label_folder_btn, 0, 1, 1, 1)
        self.next_btn = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.next_btn.setObjectName(_fromUtf8("next_btn"))
        self.gridLayout_4.addWidget(self.next_btn, 1, 1, 1, 1)
        self.imageComboBox = QtWidgets.QComboBox(self.dockWidgetContents_2)
        self.imageComboBox.setObjectName(_fromUtf8("imageComboBox"))
        self.gridLayout_4.addWidget(self.imageComboBox, 2, 0, 1, 2)
        self.browse_btn = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.browse_btn.setObjectName(_fromUtf8("browse_btn"))
        self.gridLayout_4.addWidget(self.browse_btn, 0, 0, 1, 1)
        self.autoload_chk = QtWidgets.QCheckBox(self.dockWidgetContents_2)
        self.autoload_chk.setChecked(True)
        self.autoload_chk.setObjectName(_fromUtf8("autoload_chk"))
        self.gridLayout_4.addWidget(self.autoload_chk, 4, 1, 1, 1)
        self.prev_btn = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.prev_btn.setObjectName(_fromUtf8("prev_btn"))
        self.gridLayout_4.addWidget(self.prev_btn, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)
        self.image_index_label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.image_index_label.setObjectName(_fromUtf8("image_index_label"))
        self.gridLayout_4.addWidget(self.image_index_label, 3, 1, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.gridLayout_4.addWidget(self.save_btn, 5, 0, 1, 2)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        self.verticalLayout_2.addWidget(self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.static_label1 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.static_label1.setObjectName(_fromUtf8("static_label1"))
        self.gridLayout_5.addWidget(self.static_label1, 1, 0, 1, 1)
        self.item_label_txt = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.item_label_txt.setObjectName(_fromUtf8("item_label_txt"))
        self.gridLayout_5.addWidget(self.item_label_txt, 1, 1, 1, 1)
        self.opacityBox = QtWidgets.QGroupBox(self.dockWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opacityBox.sizePolicy().hasHeightForWidth())
        self.opacityBox.setSizePolicy(sizePolicy)
        self.opacityBox.setObjectName(_fromUtf8("opacityBox"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.opacityBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.opacity_slider = QtWidgets.QSlider(self.opacityBox)
        self.opacity_slider.setMaximum(255)
        self.opacity_slider.setProperty("value", 50)
        self.opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.opacity_slider.setObjectName(_fromUtf8("opacity_slider"))
        self.verticalLayout_3.addWidget(self.opacity_slider)
        self.gridLayout_5.addWidget(self.opacityBox, 0, 0, 1, 2)
        self.dockWidget_2.setWidget(self.dockWidgetContents_3)
        self.verticalLayout_2.addWidget(self.dockWidget_2)
        self.imagecontrol_widget = QtWidgets.QDockWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagecontrol_widget.sizePolicy().hasHeightForWidth())
        self.imagecontrol_widget.setSizePolicy(sizePolicy)
        self.imagecontrol_widget.setObjectName(_fromUtf8("imagecontrol_widget"))
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.brightness_box = QtWidgets.QGroupBox(self.dockWidgetContents_5)
        self.brightness_box.setObjectName(_fromUtf8("brightness_box"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.brightness_box)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.brightness_slider = QtWidgets.QSlider(self.brightness_box)
        self.brightness_slider.setMinimum(-100)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName(_fromUtf8("brightness_slider"))
        self.horizontalLayout.addWidget(self.brightness_slider)
        self.verticalLayout.addWidget(self.brightness_box)
        self.contrast_box = QtWidgets.QGroupBox(self.dockWidgetContents_5)
        self.contrast_box.setObjectName(_fromUtf8("contrast_box"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.contrast_box)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.contrast_slider = QtWidgets.QSlider(self.contrast_box)
        self.contrast_slider.setMinimum(-100)
        self.contrast_slider.setMaximum(100)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setObjectName(_fromUtf8("contrast_slider"))
        self.horizontalLayout_2.addWidget(self.contrast_slider)
        self.verticalLayout.addWidget(self.contrast_box)
        self.imagecontrol_widget.setWidget(self.dockWidgetContents_5)
        self.verticalLayout_2.addWidget(self.imagecontrol_widget)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.gridLayout_3.addWidget(self.frame, 0, 3, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        self.menuHere = QtWidgets.QMenu(self.menubar)
        self.menuHere.setObjectName(_fromUtf8("menuHere"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionBrowse = QtWidgets.QAction(MainWindow)
        self.actionBrowse.setObjectName(_fromUtf8("actionBrowse"))
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(_fromUtf8("actionOpen_Folder"))
        self.actionLoad_Label = QtWidgets.QAction(MainWindow)
        self.actionLoad_Label.setObjectName(_fromUtf8("actionLoad_Label"))
        self.actionSave_Label = QtWidgets.QAction(MainWindow)
        self.actionSave_Label.setObjectName(_fromUtf8("actionSave_Label"))
        self.actionExit_3 = QtWidgets.QAction(MainWindow)
        self.actionExit_3.setObjectName(_fromUtf8("actionExit_3"))
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionOpen_Folder)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionLoad_Label)
        self.menuFIle.addAction(self.actionSave_Label)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionExit_3)
        self.menuHere.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuHere.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pychet Cricle Annotator", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Navigation", None))
        self.autosave_chk.setText(_translate("MainWindow", "AutoSave", None))
        self.label_folder_btn.setText(_translate("MainWindow", "Label Folder", None))
        self.next_btn.setText(_translate("MainWindow", ">", None))
        self.browse_btn.setText(_translate("MainWindow", "Image Folder", None))
        self.autoload_chk.setText(_translate("MainWindow", "AutoLoad", None))
        self.prev_btn.setText(_translate("MainWindow", "<", None))
        self.label.setText(_translate("MainWindow", "Image Index:", None))
        self.image_index_label.setText(_translate("MainWindow", "0/0", None))
        self.save_btn.setText(_translate("MainWindow", "Save", None))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Labelling Controls", None))
        self.static_label1.setText(_translate("MainWindow", "Current Label:", None))
        self.item_label_txt.setText(_translate("MainWindow", "1", None))
        self.opacityBox.setTitle(_translate("MainWindow", "Label Opacity: 50", None))
        self.imagecontrol_widget.setWindowTitle(_translate("MainWindow", "Image Controls", None))
        self.brightness_box.setTitle(_translate("MainWindow", "Brightness: 0", None))
        self.contrast_box.setTitle(_translate("MainWindow", "Contrast: 0", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Item", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Location", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Size", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Label ID", None))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Label Name", None))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle", None))
        self.menuHere.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionBrowse.setText(_translate("MainWindow", "Browse", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder", None))
        self.actionLoad_Label.setText(_translate("MainWindow", "Load Label", None))
        self.actionSave_Label.setText(_translate("MainWindow", "Save Label", None))
        self.actionExit_3.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

