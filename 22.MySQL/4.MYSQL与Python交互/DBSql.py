# -*- coding: utf-8 -*-
import pymysql 

class DBSql():
    def __init__(self,host,user,passwd,dbName,charset):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName
        self.charset = charset
    
    def connect(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbName,charset = self.charset)
        self.cursor = self.db.cursor()
        
    def close(self):
        self.cursor.close()  
        self.db.close()
    
    def getAll(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall() 
        except:
            print("查询失败")
        self.close()
        return res
    
    def insert(self,sql):
        self.__edit(sql)
    def update(self,sql):
        self.__edit(sql)
    def delete(self,sql):
        self.__edit(sql)
    
    def __edit(self,sql):
        #count = 0
        try:
            self.connect()
            self.cursor.execute(sql)
            self.db.commit()
            print("事物提交成功")
        except:
            print("事物提交失败")
            self.db.rollback()
        self.close()
        #return count
    




































