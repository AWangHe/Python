# -*- coding: utf-8 -*-
'''
break语句：
作用：跳出for和while循环
注意：只能跳出距离它最近的那一层循环

'''
num = 1
while num <= 10:
    print(num)
    if num == 3:
        break
    num += 1
#注意：循环语句可以有else语句，break导致循环截止，不会执行else下面的语句
else:
    print("sunck is a good man ! ")