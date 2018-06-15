# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")

'''
文本控件，用于显示多行文本

'''
#height 表示显示的行数
text = tkinter.Text(win, width=10, height=10)
text.pack()
str = '''Every day is a new day.Every day is a new day.Every day is a new day.
       Every day is a new day.Every day is a new day.Every day is a new day.
       Every day is a new day.Every day is a new day.Every day is a new day.
       Every day is a new day.'''
text.insert(tkinter.INSERT, str)


win.mainloop()









































