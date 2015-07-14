#-*- coding: utf-8 -*-
import const
from ConfigParser import ConfigParser

class ConfigHelper:
    SEC_UPLOAD = "upload"
    SEC_UI = "ui"
    KEY_HEX = "hex"
    KEY_COM = "port"
    KEY_BOARD = "board"
    KEY_STYLE = "style"
    KEY_PROGPAPER = "progpaper"
    
    def __init__(self, ui, cfgini=const.config):
        self.ui = ui
        self.cfgini = cfgini
        self.cfg = ConfigParser()
        self.readCfg()
        
    def readCfg(self):
        return len(self.cfg.read(self.cfgini)) > 0
    
    def getVal(self, section, key):
        if not self.cfg.has_section(section):
            return ""
        if not self.cfg.has_option(section, key):
            return ""
        
        return self.cfg.get(section, key).strip()
    
    def setVal(self, section, key, val):
        if not self.cfg.has_section(section):
            self.cfg.add_section(section)
            
        self.cfg.set(section, key, val)
    
    def writeCfg(self):
        try:
            self.cfg.write(open(self.cfgini, "w"))
        except IOError:
            pass
            
    def __updateUiAboutUpload(self):
        hex = self.getVal(self.SEC_UPLOAD, self.KEY_HEX)
        if hex != "":
            self.ui.hexfileCombox.addItem(hex)
        
        board = self.getVal(self.SEC_UPLOAD, self.KEY_BOARD)
        if board != "":
            index = self.ui.mcuCombox.findText(board)
            if index != -1:
                self.ui.mcuCombox.setCurrentIndex(index)

        com = self.getVal(self.SEC_UPLOAD, self.KEY_COM)
        if com != "":
            index = self.ui.portCombox.findText(com)
            if index != -1:
                self.ui.portCombox.setCurrentIndex(index)
            else:
                self.ui.portCombox.addItem(com)
                self.ui.portCombox.setCurrentIndex(self.ui.portCombox.count() - 1)
    
    def __updateUiAboutUi(self):
        style = self.getVal(self.SEC_UI, self.KEY_STYLE)
        if style != "":
            from PyQt4.QtGui import QApplication
            QApplication.setStyle(style)
        
        progpaper = self.getVal(self.SEC_UI, self.KEY_PROGPAPER)
        if progpaper != "":
            from os import path as OSPath
            from PyQt4.QtGui import QPixmap
            progpaper = unicode(progpaper, "gbk")
            if OSPath.exists(progpaper):
                self.ui.headLabel.setPixmap(QPixmap(progpaper).scaled(const.width, const.height))
    
    def updateUiByConfig(self):
        self.__updateUiAboutUpload()
        self.__updateUiAboutUi()
    
    def updateConfig(self, hex="", com="", board=""):
        self.setVal(self.SEC_UPLOAD, self.KEY_HEX, hex)
        self.setVal(self.SEC_UPLOAD, self.KEY_COM, com)
        self.setVal(self.SEC_UPLOAD, self.KEY_BOARD, board)
        self.writeCfg()
    