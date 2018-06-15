# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

#<ButtonRelease-1>  释放鼠标左键
#<ButtonRelease-2>  释放鼠标中键
#<ButtonRelease-3>  释放鼠标右键
label = tkinter.Label(win, text="sunck is a good man ", bg="red")
label.pack()
def func(event):
    print(event.x, event.y)
label.bind("<ButtonRelease-1>",func)


win.mainloop()









































