# -*- coding: utf-8 -*-
'''
特点：把参数进行打包，单独进行传输
优点：数据量大，安全（当对服务器数据进行修改时建议使用POST）
缺点:速度慢
'''
import urllib.request
import urllib.parse

#将要发送的数据合成一个字典
#字典的键去网站里找，一般为input标签的name属性
url = "http://www.sunck.wang:8085/form"
data = {
        "username":"sunck",
        "passwd":"666"
 }
#对要发送的数据进行打包,记住编码
postData = urllib.parse.urlencode(data).encode("utf-8")
#请求体
req = urllib.request.Request(url,data=PostData)
#请求
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)











