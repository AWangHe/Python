# -*- coding: utf-8 -*-
'''
tuple
本质：是一种有序集合

特点：  比较安全
1.与列表非常相似
2.一旦初始化就不能修改
3.使用小括号

'''
#创建元组
#格式：元组名 = (元组元素1，元组元素2，……，元组元素n)

#创建空的元组
tuple1 = ()
print(tuple1)

#创建带有元素的元组
#元组中元素的类型可以不同
tuple2 = (1,2,3,"good",True)
print(tuple2)

#定义只有一个元素的元组
tuple3 = (1, )
print(tuple3)
print(type(tuple3))

#元组元素的访问
#格式：元组名[下标]   下标从零开始
#取值
tuple4 = (1,2,3,4,5,6)
print(tuple4[0])
#获取最后一个元素
print(tuple4[-1])

#修改元组
#元组不可变指的是元组内的元素不可变，如果元组内的元素是可变的，这个元素里的内容可以变
tuple5 = (1,2,3,4,5,[6,7,8])
#tuple5[0] = 100  #报错，元组不能变
tuple5[-1][0] = 200
print(tuple5)

#删除元组
tuple6 = (1,2,3,4,5,6)
del tuple6

#元组的操作

tuple7 = (1,2,3)
tuple8 = (4,5,6)
tuple9 = tuple7 + tuple8
print(tuple9) 

#元组重复
tuple10 = (1,2,3)
print(tuple10*3)

#判断元素是否在元组中
tuple11 = (1,2,3,4,5)
print(1 in tuple11)

#元素的截取
#格式：元组名[开始下标:结束下标]
#从开始下标开始截取，截取到结束下标之前

tuple12 = (1,2,3,4,5,6,7,8,9)
print(tuple12[3:7])
print(tuple12[:7])
print(tuple12[3:])

#二维元组：元素为一维元组的元组
tuple13 = ((1,2,3),(4,5,6),(7,8,9))
print(tuple13[1][1])

#元组的方法
#len()   返回元组中元素的个数
t14 = (1,2,3,4,5)
print(len(t14))

#max()  返回元组中的最大值
#min()  返回元组中的最小值
print(max((1,2,3,4,5,6)))
print(min((1,2,3,4,5,6)))

#将列表转化为元组
list = [1,2,3,4,5,6]
t15 = tuple(list)
print(t15)

#元组的遍历
for i in (1,2,3,4,5,6):
    print(i)




















































































