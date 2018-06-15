# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

#菜单条
menubar = tkinter.Menu(win)

#菜单
menu = tkinter.Menu(menubar, tearoff=False)

#给菜单选项添加内容
for item in ["Python", "PHP", "JSP", "C", "C++", "Java", "HTML", "CSS", "JS", "退出"]:
    menu.add_command(label=item)

menubar.add_cascade(label="语言", menu=menu) 

def showMenu(event):
    #鼠标右键在哪儿显示菜单
    menubar.post(event.x_root, event.y_root)

win.bind("<Button-3>", showMenu)
win.mainloop()





























