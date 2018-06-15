# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

def update():
    print(r.get())

#一组单选框要绑定同一个变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=update)
radio1.pack()

radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=update)
radio2.pack()

win.mainloop()




















