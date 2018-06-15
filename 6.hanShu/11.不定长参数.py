# -*- coding: utf-8 -*-
'''
概念：能处理比定义时更多的参数

'''

#加了星号(*)的变量存放所有为命名的参数,如果在函数调用时没有给定参数，它就是一个空元组
def func(name,*args):
    print(name)
    for x in args:
        print(x)
func("name","age","hobby")





#**代表参数的键值对的字典，和* 所代表的的意义类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))
func2(x=1,y=2,z=3 )


def func3(*args,**kwargs):
    pass






































