# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")



def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)
win.bind("a",func)




win.mainloop()









































