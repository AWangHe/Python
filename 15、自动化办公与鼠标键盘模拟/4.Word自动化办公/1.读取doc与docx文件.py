# -*- coding: utf-8 -*-
import win32com
import win32com.client

def readWordFile(path):
    #调用系统Word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    #关闭文件
    doc.Close()
    #退出Word
    mw.Quit()
    

    
    
path = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\4.Word自动化办公\001.docx"    
readWordFile(path)































