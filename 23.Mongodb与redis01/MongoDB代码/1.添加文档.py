# -*- coding: utf-8 -*-
from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#添加文档
#插入一条
#collection.insert({"name":"wanghe", "age":20, "gender":1, "address":"北京", "isDelete":0})
#插入多条
collection.insert([{"name":"wangqi", "age":20, "gender":1, "address":"北京", "isDelete":0},{"name":"wanghao", "age":20, "gender":1, "address":"北京", "isDelete":0}])

#断开连接
conn.close()




























