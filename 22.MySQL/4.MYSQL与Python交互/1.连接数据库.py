# -*- coding: utf-8 -*-
import pymysql 

#参数1：mysql服务所在主机的IP
#参数2：用户名
#参数3：密码
#参数4：要连接的数据库名
db = pymysql.connect("localhost","root","root","sunck")

#创建一个cursor对象
cursor = db.cursor()

sql = "select version()"

#执行SQL语句
cursor.execute(sql)
#获取返回的信息
data=cursor.fetchone()
print(data)
#断开连接
cursor.close()
db.close()


























