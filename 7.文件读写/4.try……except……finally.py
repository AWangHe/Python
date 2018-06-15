# -*- coding: utf-8 -*-

'''
try……except……finally

格式：
try:
    语句t
except 错误码  as e:
    语句1
except 错误码  as e:
    语句2
……
except 错误码  as e:
    语句n
finally:
    语句f

作用：语句t是否有错误，都将会执行最后的语句f
    
'''

try:
    print(1/0)
#except:
#    print("程序出错了")
finally:
    print("结束了")
























