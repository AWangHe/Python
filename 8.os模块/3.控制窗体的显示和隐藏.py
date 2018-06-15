# -*- coding: utf-8 -*-
import win32con
import win32gui
import time

#找出窗体的编号
#TIMWin = win32gui.FindWindow("TXGuiFoundation", "TIM")

#隐藏窗体
#win32gui.ShowWindow(TIMWin, win32con.SW_HIDE)

#time.sleep(2)

#显示窗体
#win32gui.ShowWindow(TIMWin, win32con.SW_SHOW)

while True:
    TIMWin = win32gui.FindWindow("TXGuiFoundation", "TIM")
    win32gui.ShowWindow(TIMWin, win32con.SW_HIDE)
    time.sleep(2)
    win32gui.ShowWindow(TIMWin, win32con.SW_SHOW)
    time.sleep(2)

    






























