# -*- coding: utf-8 -*-
import pymysql 


db = pymysql.connect("localhost","root","root","sunck")
cursor = db.cursor()

#检查表是否存在，如果存在就删除
cursor.execute("drop table if exists car")

#建表
sql = "create table car(id int auto_increment primary key, name varchar(20) not null, money int not null)"

cursor.execute(sql)

cursor.close()
db.close()


























