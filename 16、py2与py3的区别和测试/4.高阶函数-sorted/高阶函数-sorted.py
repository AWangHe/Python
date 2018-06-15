# -*- coding: utf-8 -*-
#排序： 冒泡 选择         快排  插入  计数器

#普通排序
list1 = [4,7,2,6,3]
list2 = sorted(list1)  #默认升序排序
print(list1)
print(list2)



#按绝对值大小排序
list3 = [4,-7,-2,6,-3,-1]
list4 = sorted(list3, key=abs)  
print(list3)
print(list4)


#降序
list5 = [4,7,2,6,3]
list6 = sorted(list5, reverse=True)  #默认升序排序
print(list5)
print(list6)


#按字符串的长度排序  key=len也可以
def myLen(str):
    return len(str)
list7 = ["a123456","b12","c12345","d1234567"]
list8 = sorted(list7, key=myLen)  #默认升序排序
print(list7)
print(list8)
























