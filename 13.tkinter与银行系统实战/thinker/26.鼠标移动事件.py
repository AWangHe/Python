# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")


#<B1-Motion>  鼠标左键移动
#<B2-Motion>  鼠标中键移动
#<B3-Motion>  鼠标右键移动
label = tkinter.Label(win, text="sunck is a good man ")
label.pack()
def func(event):
    print(event.x, event.y)
label.bind("<B1-Motion>",func)


win.mainloop()









































