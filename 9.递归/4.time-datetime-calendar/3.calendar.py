# -*- coding: utf-8 -*-
import calendar
'''
日历模块
'''

#使用

#返回指定某年某月的日历
print(calendar.month(2018, 4))


#返回指定年的日历
#print(calendar.calendar(2018))


#判断一个年份是否是闰年，闰年返回True，否者返回False
#print(calendar.isleap(2018))


#返回某个月的weekday的第一天和这个月所有的天数
print(calendar.monthrange(2018, 4))


#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2018,4))























