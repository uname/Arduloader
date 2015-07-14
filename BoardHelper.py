#-*- coding: utf-8 -*-
import const
from re import search as ReSearch

def __parseBoards(fp):
    boardsinfo = {}
    cur_board_name = ""
    for line in fp.readlines():
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue
        value = line.split("=")[-1]
        if ReSearch(const.boards_name_matcher, line):
            cur_board_name = value
            boardsinfo[cur_board_name] = {}
        if cur_board_name == "":
            continue
            
        if ReSearch(const.boards_upload_protocol_matcher, line):
            boardsinfo[cur_board_name]["protocol"] = value
        if ReSearch(const.boards_upload_maximum_size_matcher, line):
            boardsinfo[cur_board_name]["maximum_size"] = int(value)
        if ReSearch(const.boards_upload_speed_matcher, line):
            boardsinfo[cur_board_name]["speed"] = value
        if ReSearch(const.boards_mcu_matcher, line):
            boardsinfo[cur_board_name]["mcu"] = value
    
    return boardsinfo
    
def getBoardsInfo():
    try:
        fp = open(const.boards_txt, "r")
        boardsinfo = __parseBoards(fp)
        fp.close()
        return True, boardsinfo
    except Exception, e:
        return False, repr(e)