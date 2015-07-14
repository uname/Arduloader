#-*- coding: utf-8 -*-
from os import path as OSPath
from Ui_MainWindow import Ui_MainWindow
from Uploader import Uploader
from PortManager import PortManager
from ConfigHelper import ConfigHelper
from icons import *
import const
import BoardHelper

from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QPixmap, QBitmap
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QColor
from PyQt4 import QtGui
from PyQt4 import QtCore

tostr = lambda qstr: qstr.toUtf8().data()
togbk = lambda qstr: unicode(tostr(qstr), "utf-8").encode("gbk")

class ArduloaderWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.portManager = PortManager(self.ui, startmonitor=True)
        self.configHelper = ConfigHelper(self.ui)
        self.initSignal()
        self.setupUi_Ex()        
               
    def setupUi_Ex(self):
        self.setWindowTitle(const.windowtitle)
        self.ui.textEdit.append(const.aboutinfo)
        self.ui.headLabel.setPixmap(QPixmap(":/main/icons/main/arduloader.png"))
        self.setWindowIcon(QtGui.QIcon(":/main/icons/main/logo.png"))
        self.setBoards()
        
        self.configHelper.updateUiByConfig()
    
    def setBoards(self):
        ret, self.__boardsinfodict = BoardHelper.getBoardsInfo()
        if not ret:
            self.__boardsinfodict = {}
            return
            
        for boardname in self.__boardsinfodict.keys():
            self.ui.mcuCombox.addItem(boardname)

    def onUploadFinish(self, ret, text):
        self.timer.stop()
        try:
            res = ret == 0 and "Upload SUCCESS:)" or ("%s\nUpload FAILED:(" % text)
        except IOError:
            res = "Read tmp file error"
        except:
            res = "Unknown error"
            
        self.ui.textEdit.append(res)
    
    def onUploading(self):
        prev_cursor = self.ui.textEdit.textCursor()
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.textEdit.insertPlainText (".")
        self.ui.textEdit.setTextCursor(prev_cursor)
    
    def getUploadArgs(self):
        infodict = self.__boardsinfodict.get(tostr(self.ui.mcuCombox.currentText()))
        if not infodict:
            return
            
        mcu = infodict["mcu"]
        speed = infodict["speed"]
        protocol = infodict["protocol"]
        maximum_size = infodict["maximum_size"]
        comport = tostr(self.ui.portCombox.currentText())
        flash_bin = togbk(self.ui.hexfileCombox.currentText())
        
        return {"mcu": mcu,
                "speed": speed,
                "protocol": protocol,
                "maximum_size": maximum_size,
                "comport": comport, 
                "flash_bin": flash_bin
                }
    
    def checkUploadArgs(self, argsdict):
        if not argsdict:
            self.ui.textEdit.append("Get chip data error")
            return False
            
        if not OSPath.exists(argsdict.get("flash_bin", "")):
            self.ui.textEdit.append("Hex file not exists")
            return False
            
        # TODO: 检查文件大小是否超多当前芯片允许的最大值
        return True
        
    def startUpload(self):
        argsdict = self.getUploadArgs()
        if not self.checkUploadArgs(argsdict):
            return
            
        self.uploader = Uploader()
        self.connect(self.uploader.qobj, QtCore.SIGNAL(const.finish_sig), self.onUploadFinish)
        self.uploader.resetUploadArgs(argsdict)
        
        self.ui.textEdit.clear()
        self.ui.textEdit.append("Start uploading\n")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.onUploading)
        self.uploader.start()
        self.timer.start(const.process_interval)
    
    def onOpenHexFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Choose a HEX file", ".", "HEX (*.hex)")
        if filename == "":
            return
        index = self.ui.hexfileCombox.findText(filename)
        if index < 0:
            self.ui.hexfileCombox.insertItem(0, filename)
            index = 0
        self.ui.hexfileCombox.setCurrentIndex(index)
    
    def closeEvent(self, e):
        hex = tostr(self.ui.hexfileCombox.currentText())
        com = tostr(self.ui.portCombox.currentText())
        board = tostr(self.ui.mcuCombox.currentText())
        self.configHelper.updateConfig(hex, com, board)
        e.accept()
        
    def initSignal(self):
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.uploadButton.clicked.connect(self.startUpload)
        self.ui.openHexButton.clicked.connect(self.onOpenHexFile)
        
