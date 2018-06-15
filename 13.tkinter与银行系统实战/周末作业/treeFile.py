# -*- coding: utf-8 -*-
import tkinter
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows
win = tkinter.Tk()
win.title("魔兽世界")
win.geometry("900x400+200+300")

path = r"F:\Python\教学视频"

infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path,infoWin)

win.mainloop()

 