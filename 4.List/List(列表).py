# -*- coding: utf-8 -*-
#拷贝
#浅拷贝   引用拷贝
list27 = [1,2,3,4,5]
list28 = list27
list27[1] = 200
print(list27)
print(list28)
print(id(list27))
print(id(list28))

#深拷贝  内存拷贝
list29 = [1,2,3,4,5]
list30 = list29.copy()
list29[1] = 200
print(list29)
print(list30)
print(id(list29))
print(id(list30))

#将元组转化为列表
list31 = list((1,2,3,4,5))
print(list31)