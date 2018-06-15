# -*- coding: utf-8 -*-
'''
概述：
使用键-值（key-value）存储，具有极快的查找速度

注意：字典是无序的

key的特性：
1.字典中的key必须唯一
2.key必须是不可变对象
3.字符串、整数等都是不可变的，可以作为key
4.list是可变的，不能作为key

思考：保存多位学生的姓名与成绩
使用字典：学生姓名为key，学生成绩作为值 


字典和list的比较：
字典：
1.查找和插入的速度极快，不会随着key-value的增加而变慢
2.需要占用大量的内存，内存浪费多

list:
1.查找和插入的速度随着数据量的增加而变慢
2.占用的空间小，浪费的内存少


'''
dict1 = {"tom":60,"lilei":70}

#元素的访问
#获取：字典名[key]
print(dict1["lilei"])
#print(dict1["sunck"])  #没有
print(dict1.get("sunck"))
ret = dict1.get("sunck")
if ret == None:
    print("没有")
else:
    print("有")


#添加
dict1["hanmeimei"] = 99
#因为一个key对应一个value，所以多次对一个key的赋值其实就是修改值
dict1["lilei"] = 100
print(dict1)

#删除
#dict1.pop("tom")
#print(dict1)


#遍历
for key in dict1:
    print(key,dict1[key])
    
for value in dict1.values():  #[60,100,99]
    print(value)
    
for k,v in dict1.items():
    print(k,v)

for i,v in enumerate(dict1):
    print(i,v)


#查找一个字符串在另一个字符串中出现的次数

#w = "good"
#str = "sunck is a good man! sunck is a nice man!  sunck is a noble man!"
#print(str.count(w))


w = input()
str = "sunck is a good man! sunck is a nice man!  sunck is a noble man!"
d = {}
l = str.split(" ")
for v in l:
    c = d.get(v)
    if c == None:
        d[v] = 1
    else:
        d[v] += 1
print(d[w])

'''
1.以空格切割字符串
2.循环处理列表中的每个元素
3.以元素当做key去列表中提取数据
4.如果没有提取到，就以该元素作为key，1作为value存进字典
5.如果提取到，将对应的key的value修改，值加1
6.根据输入的字符串当做key再去字典取值
'''




































