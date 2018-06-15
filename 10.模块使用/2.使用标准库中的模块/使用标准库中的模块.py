# -*- coding: utf-8 -*-
#引入模块
import sys 

print(sys.argv)

#获取命令行的参数列表
for i in sys.argv:
    print(i)
    

name = sys.argv[1]
age  = sys.argv[2]
hobby = sys.argv[3]


#自动查找所需模块的路径的列表
print(sys.path)

























