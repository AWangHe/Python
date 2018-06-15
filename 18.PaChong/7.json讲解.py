# -*- coding: utf-8 -*-
'''
概念：一种保存数据的格式
作用：可以保存本地的json 文件，也可以将json串进行传输，
   通常将json称为轻量级的传输方式
json文件组成：
{}   代表对象
[]   代表列表
:    代表键值对
,    分隔两个部分
'''
'''
1.loads针对内存对象，即将Python内置数据序列化为字串
2.load针对文件句柄
3.dumps
4.dump
json.dumps : dict转成str   
json.dump是将python数据保存成json

json.loads:str转成dict          
json.load是读取json数据 
'''
import json

jsonStr = '''{
          "name":"菜鸟教程",
          "url":"www.runoob.com", 
          "slogan":"学的不仅是技术，更是梦想！"
          }'''
#将json格式的字符串转化为Python数据类型的对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["name"])

#将Python数据类型的对象转化为json格式的字符串
jsonData2 = {
          "name":"cainiaojiaocheng",
          "url":"www.runoob.com", 
          "slogan":"dream"
          }
jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)
print(type(jsonStr2))

#读取本地的json文件
path1 = r"F:\Python\Test\test.json"
with open(path1,"rb") as f:
    data = json.load(f)
    print(data)
    print(type(data))

#写本地的json文件
path2 = r"F:\Python\Test\test2.json"
jsonData3 = {
          "name":"cainiaojiaocheng",
          "url":"www.runoob.com", 
          "slogan":"dream"
          }   
with open(path2,"w") as f:
    json.dump(jsonData3,f)











