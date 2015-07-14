#-*- coding: utf-8 -*-
from PyQt4.QtCore import QObject, SIGNAL
import const
import os
import threading

def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    pipe = os.popen(cmd + ' 2>&1', 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None: sts = 0
    if text[-1:] == '\n': text = text[:-1]
    return sts, text
    
class Uploader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.qobj = QObject()
        
        self.avrdude = const.avrdude
        self.avrdude_conf = const.avrconf
        self.mcu = 'atmega328p'
        self.speed = "115200"
        self.protocol = "arduino"
        self.comport = "COM3"
        self.flash_bin = ''
        
        self.__buildUploadCmd()
    
    def __buildUploadCmd(self):
        self.upload_cmd = "%s -C%s -v -p%s -c%s -P%s -b%s -D -Uflash:w:%s:i 2>%s" % (
                           self.avrdude,
                           self.avrdude_conf,
                           self.mcu,
                           self.protocol,
                           self.comport,
                           self.speed,
                           self.flash_bin,
                           const.arduloader_log)
    
    def resetUploadArgs(self, argsdict):
        assert type(argsdict) is dict
        
        self.mcu = argsdict["mcu"]
        self.speed = argsdict["speed"]
        self.protocol = argsdict["protocol"]
        self.comport = argsdict["comport"]
        self.flash_bin = argsdict["flash_bin"]
        
        self.__buildUploadCmd()
        
    def run(self):
        self.upload()
        
    def upload(self):
        ret, text = getstatusoutput(self.upload_cmd)
        self.qobj.emit(SIGNAL(const.finish_sig), ret, text)
        