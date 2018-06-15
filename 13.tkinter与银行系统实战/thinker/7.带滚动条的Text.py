# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
#win.geometry("400x400+400+100")

#创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=50, height=8)
#side放到窗体的那一侧   fill填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


str = '''Every single time you access a website, you leave tracks. 
       Tracks that others can access. If you don't like the idea, 
       find out what software can help you cover them.
       Anti Tracks
      Anti Tracks is a complete solution to protect your privacy and enhance 
      your PC performance. With a simple click Anti Tracks securely 
      erase your internet tracks, computer activities and 
      programs history information stored in many hidden files 
      on your computer.Anti Tracks support Internet Explorer, AOL,
      Netscape/Mozilla and Opera browsers. It also include more than 
      85 free plug-ins to extend erasing features to support popular
      programs such as ACDSee, Acrobat Reader, KaZaA, PowerDVD, WinZip, 
      Free Download: http://www.deprice.com/antitracks.htm'''
text.insert(tkinter.INSERT, str)


win.mainloop()









































