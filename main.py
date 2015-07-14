#-*- coding: utf-8 -*-
#Author:    Uname
#Date:      2014/2/11
#Version:   0.2
#Copyright: uname.github.io

import sys
sys.dont_write_bytecode = True
from ArduloaderWindow import ArduloaderWindow
from PyQt4.QtGui import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("cleanlooks")
    window = ArduloaderWindow()
    window.show()
    sys.exit(app.exec_())
