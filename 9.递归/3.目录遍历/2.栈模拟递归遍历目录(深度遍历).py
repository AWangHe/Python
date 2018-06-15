# -*- coding: utf-8 -*-
import os 

def getAllDirDeep(path):
    stack = []
    stack.append(path)
    
    
    #处理栈，当栈为空时结束循环
    while len(stack) != 0:
        #从栈里取出数据
        dirPath = stack.pop()
        #目录下所有文件
        filesList = os.listdir(dirPath)
        #处理每一个文件，如果是普通文件则打印出来，如果是目录则将该目录的地址压栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录：" + fileName)
                stack.append(fileAbsPath)
            else:
                #是文件就打印
                print("文件：" + fileName)
        
getAllDirDeep(r"F:\Python\教学视频")       
    






























