#-*- coding: utf-8 -*-
import serial.tools.list_ports as lp
from PyQt4.QtCore import QTimer

class PortManager(object):
    def __init__(self, ui, queryinterval=1000, startmonitor=False):
        self.ui = ui
        self.queryinterval = queryinterval
        self.querytimer = QTimer()
        self.querytimer.timeout.connect(self.__updateUiComPorts)
        self.com_list = []
        self.__updateUiComPorts(showmsg=False)
        if startmonitor:
            self.startComPortMonitor()
        
    def __updateUiComPorts(self, com_list=None, showmsg=True):
        if com_list is None:
            com_list = self.__getComInfoList()
        
        # NEW ADDED
        for comport in list(set(com_list) - set(self.com_list)):
            self.ui.portCombox.addItem(comport)
            if showmsg:
                self.ui.textEdit.append("New port found: %s" % comport)
        # NEW REMOVED
        for comport in list(set(self.com_list) - set(com_list)):
            index = self.ui.portCombox.findText(comport)
            if index == -1:
                continue
            self.ui.portCombox.removeItem(index)
            if showmsg:
                self.ui.textEdit.append("Port removed: %s" % comport)
                
        self.com_list = com_list
        
    def __getComInfoList(self):
        return [tup[0] for tup in list(lp.comports())]
        
    def startComPortMonitor(self):
        self.querytimer.start(self.queryinterval)
    
    def stopComPortMonitor(self):
        self.querytimer.stop()
        