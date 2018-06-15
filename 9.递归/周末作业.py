# -*- coding: utf-8 -*-
import os 
import collections


def work(path):
    resPath = r"F:\Python\data\9.递归\res"
    #打开文件
    with open(path, "r") as f:
        while True:
            #dota8879@foxmail.com----123456
            lineInfo = f.readline()
            if len(lineInfo) < 5:
                break
            
            #邮箱的字符串
            #dota8879@foxmail.com
            mailStr = lineInfo.split("----")[0]
            #邮箱类型的目录
            #F:\Python\data\9.递归\res\foxmail
            fileType = mailStr.split("@")[1].split(".")[0]
            dirStr = os.path.join(resPath, fileType)
            if not os.path.exists(dirStr):
                #不存在目录，创建目录
                os.mkdir(dirStr)
            
            filePath = os.path.join(dirStr, fileType + ".txt")
            with open(filePath, "a") as fw:
                fw.write(mailStr + "\n")




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
            #判断是否是目录，是目录就进队，不是就处理文件
            if os.path.isdir(fileAbsPath):
                queue.append(fileAbsPath)
            else:
                #处理普通文件
                work(fileAbsPath)
                
  
getAllDirBreadth(r"F:\Python\data\9.递归\dir")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
