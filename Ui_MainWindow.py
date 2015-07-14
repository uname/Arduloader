# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/mainwindow.ui'
#
# Created: Tue Jul 14 22:43:58 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(447, 556)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.headLabel = QtGui.QLabel(self.centralwidget)
        self.headLabel.setText(_fromUtf8(""))
        self.headLabel.setObjectName(_fromUtf8("headLabel"))
        self.gridLayout.addWidget(self.headLabel, 0, 0, 1, 5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.hexfileCombox = QtGui.QComboBox(self.centralwidget)
        self.hexfileCombox.setMinimumSize(QtCore.QSize(311, 0))
        self.hexfileCombox.setEditable(True)
        self.hexfileCombox.setObjectName(_fromUtf8("hexfileCombox"))
        self.horizontalLayout.addWidget(self.hexfileCombox)
        self.openHexButton = QtGui.QPushButton(self.centralwidget)
        self.openHexButton.setObjectName(_fromUtf8("openHexButton"))
        self.horizontalLayout.addWidget(self.openHexButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 5)
        self.portCombox = QtGui.QComboBox(self.centralwidget)
        self.portCombox.setEditable(False)
        self.portCombox.setObjectName(_fromUtf8("portCombox"))
        self.gridLayout.addWidget(self.portCombox, 2, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet(_fromUtf8(""))
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 5)
        spacerItem = QtGui.QSpacerItem(260, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 3)
        self.uploadButton = QtGui.QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.gridLayout.addWidget(self.uploadButton, 4, 3, 1, 1)
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.gridLayout.addWidget(self.exitButton, 4, 4, 1, 1)
        self.mcuCombox = QtGui.QComboBox(self.centralwidget)
        self.mcuCombox.setEnabled(True)
        self.mcuCombox.setEditable(False)
        self.mcuCombox.setObjectName(_fromUtf8("mcuCombox"))
        self.gridLayout.addWidget(self.mcuCombox, 2, 1, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Arduloader", None, QtGui.QApplication.UnicodeUTF8))
        self.openHexButton.setText(QtGui.QApplication.translate("MainWindow", "Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadButton.setText(QtGui.QApplication.translate("MainWindow", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

