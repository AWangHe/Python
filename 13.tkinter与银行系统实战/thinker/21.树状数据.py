# -*- coding: utf-8 -*-
import tkinter 
from tkinter import ttk
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小600x400  距离左侧400，距离上侧100
win.geometry("600x400+400+100")


tree = ttk.Treeview(win)
tree.pack()

#添加一级树枝
treeF1 = tree.insert("",0,"中国",text="中国CHI",values=("F1"))
treeF2 = tree.insert("",1,"美国",text="美国USA",values=("F2"))
treeF3 = tree.insert("",2,"英国",text="英国UK",values=("F3"))

#添加二级树枝
treeF1_1 = tree.insert(treeF1,0,"黑龙江",text="中国黑龙江",values=("F1_1"))
treeF1_2 = tree.insert(treeF1,1,"吉林",text="中国吉林",values=("F1_2"))
treeF1_3 = tree.insert(treeF1,2,"辽宁",text="中国辽宁",values=("F1_3"))

#添加三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,"哈尔滨",text="黑龙江哈尔滨",values=("F1_1_1"))
treeF1_1_2 = tree.insert(treeF1_1,1,"五常",text="黑龙江五常",values=("F1_1_2"))

















win.mainloop()









































