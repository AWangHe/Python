# -*- coding: utf-8 -*-
import win32con
import win32gui
import random
import time

#找出窗体的编号
TIMWin = win32gui.FindWindow("TXGuiFoundation", "TIM")

'''
参数1：控制的窗体
参数2：大致方位，win32con.HWND_TOPMOST上方
参数3：位置x
参数4：位置y
参数5：长度
参数6：宽度  
'''
while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(TIMWin, win32con.HWND_TOPMOST, x, y, 300, 300, win32con.SWP_SHOWWINDOW)



























