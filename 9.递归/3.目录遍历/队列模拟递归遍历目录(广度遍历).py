# -*- coding: utf-8 -*-
import os 
import collections

def getAllDirBreadth(path):
    queue = collections.deque()
    #进队
    queue.append(path)
    
    while len(queue) != 0:
        #出队
        dirPath = queue.popleft()
        #找出所有文件
        filesList = os.listdir(dirPath)
        
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            #判断是否是目录，是目录就进队，不是就打印
            if os.path.isdir(fileAbsPath):
                print("目录："+fileName)
                queue.append(fileAbsPath)
            else:
                print("普通文件："+fileName)
    
getAllDirBreadth(r"F:\Python\教学视频")  































