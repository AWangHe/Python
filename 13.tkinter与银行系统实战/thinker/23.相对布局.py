# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

label1=tkinter.Label(win,text="good",bg="blue")
label2=tkinter.Label(win,text="nice",bg="yellow")
label3=tkinter.Label(win,text="cool",bg="red")

#相对布局  窗口的变化对控件的位置有影响
#tkinter.BOTH   ===  tkinter.Y
label1.pack(fill=tkinter.Y,side=tkinter.LEFT)
label2.pack(fill=tkinter.X,side=tkinter.TOP)
label3.pack()





win.mainloop()









































