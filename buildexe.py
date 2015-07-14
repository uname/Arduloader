#-*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

includes = ["sip", "PyQt4.QtGui", "PyQt4.QtCore"]
            
dll_excludes = ["msvcm90.dll", "msvcp90.dll", "msvcr90.dll"]

setup(  version="0.1",
        description = "Arduino Hex Uploader",
        name = "arduloader.exe",
        author = "Apache",
        zipfile = None,
        windows = [{"script":"main.py", "icon_resources":[(1, "./icons/main/logo.ico")]}],
		options = {   "py2exe":
                        {   "compressed": 2,
                            "bundle_files": 1,
                            "includes": includes,
                            "dll_excludes":dll_excludes
                        }
                })
