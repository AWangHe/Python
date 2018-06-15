# -*- coding: utf-8 -*-
#win + r --->  regedit  ---> HKEY_CURRENT_USER  ---> Control panel  --->Desktop

import win32api
import win32con
import win32gui

def setWallPaper(path):
    #打开注册表   打开哪个注册表   打开注册表要设置数据
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    #2 拉伸  0 居中  6适应   10填充
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"2")
    #SPIF_SENDWININICHANGE   设置立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)
    
path = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\8.修改背景图片\001.jpg"
setWallPaper(path)

























