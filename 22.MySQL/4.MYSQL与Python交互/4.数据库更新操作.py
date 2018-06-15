# -*- coding: utf-8 -*-
import pymysql 


db = pymysql.connect("localhost","root","root","sunck", charset="utf8")
cursor = db.cursor()


#建表
sql = 'update car set money = 1 where name = "奥迪"'
try:
    cursor.execute(sql)
    db.commit()
    print("成功")
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()
    print("失败")

cursor.close()
db.close()


























