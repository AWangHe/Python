# -*- coding: utf-8 -*-
import os 

def getAllDir(path, sp = ""):
    #得到当前目录下的所有文件
    filesList = os.listdir(path)
    
    #处理每一个文件
    sp += "   "
    for fileName in filesList:
        #判断是否是路径(用绝对路径)
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录：", fileName)
            #递归调用
            getAllDir(fileAbsPath,sp)
        else:
            print(sp + "文件：", fileName)
    




getAllDir(r"F:\Python\教学视频")

























