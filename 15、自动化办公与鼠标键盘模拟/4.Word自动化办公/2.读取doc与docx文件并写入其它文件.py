# -*- coding: utf-8 -*-
import win32com
import win32com.client

def readWordFileToOtherFile(path, toPath):
    #调用系统Word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)
    #将Word中的数据保存到另一个文件
    #2 表示这是一个TXT文件
    doc.SaveAs(toPath,2)
    #关闭文件
    doc.Close()
    #退出Word
    mw.Quit()
    

    
    
path = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\4.Word自动化办公\001.docx" 
toPath = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\4.Word自动化办公\002.txt"     
readWordFileToOtherFile(path, toPath)































