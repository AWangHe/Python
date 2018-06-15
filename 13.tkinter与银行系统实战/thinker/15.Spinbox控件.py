# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

'''
数值范围控件

'''

def update():
    print(v.get())



#绑定个变量
v = tkinter.StringVar()
#increment  步长   默认为1
#values=(0,2,4,6,8,10) 最好不要与  from_=0  to=100   increment=1   同时使用
#command   只要值改变就会执行对应的方法
sp = tkinter.Spinbox(win, from_=0, to=100, increment=1, textvariable=v, command=update)
sp.pack()

#赋值
v.set(20)
#取值
print(v.get())











win.mainloop()






















