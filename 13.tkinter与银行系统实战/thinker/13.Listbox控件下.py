# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

#MULTIPLE支持多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()
for item in ["good", "nice", "handsome", "amazing", "interesting"]:
    #按顺序添加
    lb.insert(tkinter.END, item)


win.mainloop()




















