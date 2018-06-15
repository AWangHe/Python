# -*- coding: utf-8 -*-
import tkinter 
from tkinter import ttk
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")



#绑定变量
cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable = cv)
com.pack()
#设置下拉数据
com["value"] = ("济南", "青岛", "济宁")
#设置默认值
com.current(0)

#绑定事件
def func(event):
    print(com.get())
    print(cv.get())
com.bind("<<ComboboxSelected>>", func)





win.mainloop()









































