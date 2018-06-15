# -*- coding: utf-8 -*-
'''
格式：
for 变量名 in 集合：
  语句

逻辑：按顺序取“集合”中的每个元素赋值给“变量”，再去执行语句。如此循环往复，直到取完
     “集合”中的元素为止。

'''
#for i in [1,2,3,4,5]:
#    print(i)

'''
range([start,] end [,step])函数  列表生成器
start默认为0，step默认为1
功能：生成数列

'''
#for i in range(10):
#    print(i)
#
#for y in range(2,20,2):
#    print(y)

#同时遍历下标和元素
#index,m = 下标,元素
for index,m in enumerate([1,2,3,4,5]):
    print(index,m)
    
    
    
    
    
    
    
    
    
    
    
    
    
    