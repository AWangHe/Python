# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

'''
框架控件：
在屏幕上显示一个矩形区域，多作为容器控件

'''
frm = tkinter.Frame(win)
frm.pack()

#left
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l, text="左上", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_l, text="左下", bg="blue").pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)

#right 
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text="左上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="左下", bg="yellow").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)


win.mainloop()









































