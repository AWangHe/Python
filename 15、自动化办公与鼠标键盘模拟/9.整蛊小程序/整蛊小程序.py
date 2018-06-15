# -*- coding: utf-8 -*-
import time
import pygame
import win32api
import win32con
import win32gui
#线程模块
import threading

def go():
    pygame.mixer.init()
    while True:
        for i in range(2):
            filePath = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\9.整蛊小程序"+"\\"+str(i)+".mp3"
            track = pygame.mixer.music.load(filePath)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()


def setWallPaper(path):
    #打开注册表   打开哪个注册表   打开注册表要设置数据
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    #2 拉伸  0 居中  6适应   10填充
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"2")
    #SPIF_SENDWININICHANGE   设置立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)


th = threading.Thread(target=go, name="LoopThread")
th.start()


while True:
    for i in range(7):
        filePath = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\9.整蛊小程序"+"\\"+str(i)+".jpg"
        setWallPaper(filePath)
        time.sleep(2)
























