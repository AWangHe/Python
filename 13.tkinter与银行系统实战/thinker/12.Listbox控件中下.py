# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
#win.geometry("400x400+400+100")

#EXTENDED  可以使listbox支持shift和control
#按住shift，可以实现连选
#按住control，可以实现多选
lb = tkinter.Listbox(win, selectmode= tkinter.EXTENDED) 

for item in ["good", "nice", "handsome", "amazing", "interesting",
             "good1", "nice1", "handsome1", "amazing1", "interesting1",
             "good2", "nice2", "handsome2", "amazing2", "interesting2"]:
    #按顺序添加
    lb.insert(tkinter.END, item)

#滚动条
scroll = tkinter.Scrollbar()  
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=scroll.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
#额外给属性赋值
scroll['command'] = lb.yview     
    
    
    
    
    

win.mainloop()



























