#-*- coding: utf-8 -*-
import platform

version = "1.0Beta"
config = "config.ini"
width = 465
height = 142
windowtitle = "Arduloader"
aboutinfo = """
  __    ___   ___   _     _     ___    __    ___   ____  ___  
 / /\  | |_) | | \ | | | | |   / / \  / /\  | | \ | |_  | |_) 
/_/--\ |_| \ |_|_/ \_\_/ |_|__ \_\_/ /_/--\ |_|_/ |_|__ |_| \ 

Arduloader is tool for uploading hex file to your Arduino board
Author uname.github.com
Email hqwemail@163.com
Version %s
""" % version
if platform.system() == "Windows":
    avrdude = r'.\avrtool\avrdude.exe'
    avrconf = r'.\avrtool\avrdude.conf'
else:
    avrdude = "./avrtool/avrdude"
    avrconf = './avrtool/avrdude.conf'
    
arduloader_log = "arduloader.log"
finish_sig = "finish"
process_interval = 100 #ms

minport = 2
maxport = 40

boards_txt = "boards.txt"
boards_name_matcher = r".name\s*="
boards_upload_protocol_matcher = r".upload.protocol\s*="
boards_upload_maximum_size_matcher = r".upload.maximum_size\s*="
boards_upload_speed_matcher = r".upload.speed\s*="
boards_mcu_matcher = r".build.mcu\s*="