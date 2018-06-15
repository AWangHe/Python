# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

'''
列表框控件：可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串

'''

 #1.创建一个listbox，添加几个元素
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()
for item in ["good", "nice", "handsome", "amazing", "interesting"]:
    #按顺序添加
    lb.insert(tkinter.END, item)
#在开始添加
lb.insert(tkinter.ACTIVE, "beauty")
#将列表当成一个元素添加的
#lb.insert(tkinter.END, ["fantastic", "amazing"])

#删除  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引处的内容
#lb.delete(1)
#lb.delete(1, 3)

#选中  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只选中第一个索引处的内容
lb.select_set(2,4)
#lb.select_set(2)

#取消选中
#lb.select_clear(3,4)
#lb.select_clear(3)

#获取到列表中元素的个数
#print(lb.size())

#从列表中取值  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只获取第一个索引处的内容 
#print(lb.get(2,4))
#print(lb.get(2))

#返回当前选中的索引项，不是item元素
print(lb.curselection())

#判断一个选项是否被选中  
print(lb.select_includes(1))
print(lb.select_includes(3))





win.mainloop()
































