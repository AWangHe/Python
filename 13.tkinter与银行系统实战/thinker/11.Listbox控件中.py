# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

#绑定变量
lbv = tkinter.StringVar()
#与BROWSE相似，但是不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win, selectmode= tkinter.SINGLE, listvariable=lbv ) 
lb.pack()
for item in ["good", "nice", "handsome", "amazing", "interesting"]:
    #按顺序添加
    lb.insert(tkinter.END, item)

#打印当前列表中的选项
print(lbv.get())
#设置选项
#lbv.set(("1", "2", "3"))

#绑定事件
def myPrint(event):
    print(lb.get(lb.curselection()))
lb.bind('<Double-Button-1>', myPrint)
















win.mainloop()


















