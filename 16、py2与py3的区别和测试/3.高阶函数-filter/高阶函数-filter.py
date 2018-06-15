# -*- coding: utf-8 -*-
'''
原型：filter(fn, lsd)
参数1 为函数
参数2 为序列
功能：用于过滤序列
白话文：把传入的函数依次作用于序列的每个元素，根据返回的是True还是False决定决定是否保留该元素

'''
list1 = [1,2,3,4,5,6]
#筛选条件
def func(num):
    #偶数保留
    if num%2 == 0:
        return True
    return False
res1 = filter(func, list1)
print(list(res1))



data = [["姓名","年龄","身高","爱好"],["wh",28,180,"篮球"],["haha",28,180,"无"],["jiajia",28,180,"无"]]
def func2(v):
    v = str(v)
    if v == "无":
        return False
    return True

for line in data:
    m = filter(func2, line)
    print(list(m))
    
























