# -*- coding: utf-8 -*-
'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类代表一个进程对象


'''
from multiprocessing import Process
from time import sleep 

def run():
    while True:
        print("sunck is a nice man")
        sleep(1.2)

if __name__ == "__main__":
    print("主（父）进程启动")
    #创建子进程
    #target 说明进程执行的任务
    p = Process(target = run )
    #启动进程
    p.start()
    
   
    































