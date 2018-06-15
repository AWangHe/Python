# -*- coding: utf-8 -*-
from functools import reduce  

#python 内置了map()和reduce()


#map()
#原型  map(fn, lsd)
#参数1 是函数
#参数2 是序列
#功能：将传入的函数依次作用在序列中的每一个元素，并把结果作用在新的Iterator返回

#将单个字符转成对应的字面量整数
def chrToInt(chr):
    return {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}[chr]
list1 = ["0", "1", "2", "3"]
res = map(chrToInt, list1)
print(res)
print(list(res))

#[chrToInt("0"), chrToInt("1"), chrToInt("2"), chrToInt("3")]

#将整数元素的序列转为字符串型
#[1,2,3,4] --->  ["1","2","3","4"]
list2 = [1,2,3,4]
res2 = map(str, list2) 
print(list(res2))


#reduce(fn, lsd)
#参数1 为函数
#参数2 为列表
#功能：一个函数作用在序列上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素累计运算
#reduce(f, [a,b,c,d])
# f(f(f(a, b), c), d)

#求一个序列的和
list3 = [1,2,3,4,5,6]
def mySum(x, y):
    return x + y
res3 = reduce(mySum, list3)
print("res3 =",res3)


#将字符串转成对应字面量数字
def strToInt(str):
    def fc(x,y):
        return x * 10 + y
    def fs(chr):
        return {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}[chr]
    return reduce(fc, map(fs,list(str)))

print(strToInt("123456789"))

























