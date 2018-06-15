# -*- coding: utf-8 -*-
'''
fetchone()
功能：获取下一个查找结果集，结果集是一个对象

fetchall() 
功能：接受全部的返回的行

rowcount:是一个只读属性，返回execute()方法影响的行数

'''
import pymysql 


db = pymysql.connect("localhost","root","root","sunck", charset="utf8")
cursor = db.cursor()


#建表
sql = 'select * from car where name = "奥迪"'
try:
    cursor.execute(sql)
    
    reslist = cursor.fetchall()
    for row in reslist:
        print("%d---%s---%d" % (row[0],row[1],row[2]))
    
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()
    print("失败")

cursor.close()
db.close()







































































