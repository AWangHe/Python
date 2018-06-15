# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:06:31 2018

@author: huanj
"""

#计算水仙花数
'''
num = int(input("请输入一个三位数："))
a = num % 10
b = num //10 % 10
c = num // 100
if num == a**3 + b**3 + c**3:
    print("Yes")
else:
    print("No")
   
#输出字符串    
str = "sunck is a good man"   
index = 0
while index < len(str) :
    print("str[%d] = %s" % (index, str[index]))
    index += 1
    
#计算字符串中数字的和
str = input("请输入一个字符串：")
index = 0
sum = 0
while index < len(str):
    if str[index] >= "0" and str[index] <= "9":
        sum += int(str[index])
    index += 1
print("sum = %d" % (sum))
'''
#删除列表中的全部的某个元素
list = [1,2,3,4,5,3,3,3,4,5,6,7,8,9]
num = 0
all = list.count(3)
while num < all:
    list.remove(3)
    num += 1
print(list)








   
        
    
   