# -*- coding: utf-8 -*-
import time
'''
UTC(世界协调时间)：格林尼治天文时间，世界标准时间，在中国来说是UTC+8
DST(夏令时)：是一种节约能源而认为规定的时间制度，在夏季调快一个小时

时间的表示形式：
1.时间戳
以整形或浮点型表示时间的一个以秒为单位的时间间隔。这个时间间隔的基础值是从1970年1月1日
零点开始算起。
2.元组
一种Python的数据结构表示，这个元组有9个整形内容，
year
month
day
hours
minutes
seconds
weekday
Julia day
flag(1 或 0 或 -1)
3.格式化字符串

'''


#返回当前时间的时间戳，浮点数形式，不需要参数
c = time.time()
print(c)

#将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)

#将时间戳转为本地时间元组
b = time.localtime(c)
print(b)

#将本地时间转化为时间戳
m = time.mktime(b)
print(m)


#将时间元组转成字符串
s = time.asctime(b)
print(s)


#将时间戳转转成字符串   time.asctime(time.localtime(time.time()))
p = time.ctime(c)
print(p)


#将时间元组转换成给定格式的字符串，参数2为时间元组，如果没有参数2，默认转当前时间
q = time.strftime("%Y-%m-%d %H:%M:%S", b)
print(q)

#将时间字符串转为时间元组
w = time.strptime(q, "%Y-%m-%d %H:%M:%S")
print(w)

#延迟一个时间，整型或者浮点型
time.sleep(1)


#返回当前程序的CPU执行时间
#Unix系统始终返回全部的运行时间
#Windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数
y1 = time.clock()
print("%d" % y1)
time.sleep(2)

y2 = time.clock()
print("%d" % y2)
time.sleep(2)

y3 = time.clock()
print("%d" % y3)





























