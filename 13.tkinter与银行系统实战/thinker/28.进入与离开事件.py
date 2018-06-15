# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")


#<Enter>   鼠标光标进入控件时触发
#<Leave>   鼠标光标离开控件时触发
label = tkinter.Label(win, text="sunck is a good man ", bg="red")
label.pack()
def func(event):
    print(event.x, event.y)
label.bind("<Leave>",func)


win.mainloop()









































