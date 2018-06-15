# -*- coding: utf-8 -*-
from DBSql import DBSql

s = DBSql("localhost","root","root","sunck","utf8")

res = s.getAll('select * from car where money > 1')
for row in res:
        print("%d---%s---%d" % (row[0],row[1],row[2]))


s.insert('insert into car values(0,"奇瑞",1000000)')
s.update('update car set money = 1 where name = "奥迪"')
s.delete('delete from  car  where name = "奥迪"')


























