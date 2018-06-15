# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")
'''
Label:标签控件可以显示文本


'''
#win  父窗体
#text  显示的文本内容
#bg  背景色
#fg  字体颜色
#wraplength  指定文本中多宽之后进行换行
#justify   文本换行之后的对齐方式
#anchor  n北  e东  s南  w西  center居中  ne  nw  se  sw
label = tkinter.Label(win, text="sunck is a good man ", bg="pink", 
                      fg="red", font=("黑体", 20),
                      width=30, height=10, wraplength=100,
                      justify="left", anchor="center")

#显示出来
label.pack() 




win.mainloop()









































