# -*- coding: utf-8 -*-
import tkinter 

def func():
    print("sunck is a good man")


#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

#创建按钮
button1 = tkinter.Button(win, text="按钮", command=func, width=10, height=5)
button1.pack()

#使用匿名函数
button2 = tkinter.Button(win, text="按钮", command=lambda:print("sunck is a nice man"))
button2.pack()

win.mainloop()









































