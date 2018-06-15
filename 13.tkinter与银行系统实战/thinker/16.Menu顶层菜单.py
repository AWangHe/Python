# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

def func():
    print("WH is a good man  ")

#菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)
#创建一个菜单选项
#tearoff  False表示菜单选项不可以独立出来
menu1 = tkinter.Menu(menubar, tearoff=False)

#给菜单选项添加内容
for item in ["Python", "PHP", "JSP", "C", "C++", "Java", "HTML", "CSS", "JS", "退出"]:
    if item == "退出":
        #添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=func)
#向菜单条上添加菜单选项
menubar.add_cascade(label="语言", menu=menu1)       
    













win.mainloop()




























