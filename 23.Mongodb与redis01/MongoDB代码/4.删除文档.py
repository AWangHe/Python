# -*- coding: utf-8 -*-
from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#删除文档
collection.remove({"name":"lilei"})
#全部删除
#collection.remove()
#断开连接
conn.close()




























