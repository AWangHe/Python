# -*- coding: utf-8 -*-
import redis

#连接
r = redis.StrictRedis(host="localhost", port=6379, password="sunck")

#方法1：根据数据类型的不同，调用响应的方法
#写
#r.set("p1","good")
#r.lpush("s2",1,2,3,4,5)
#读
#print(r.get("p1"))


#方法2：pipline
#缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set("p3","nice")
pipe.set("p4","handsome")
pipe.set("p5","cool")
pipe.execute() 

























