# -*- coding: utf-8 -*-
import urllib.request
import random

url = "http://www.baidu.com"
##模拟请求头
#headers = {
#        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
#}
##设置一个请求体
#req = urllib.request.Request(url,headers=headers)
##发起请求
#response = urllib.request.urlopen(req) 
#data = response.read().decode("utf-8")
#print(data)

agentsList = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 "
]
agentStr = random.choice(agentsList)
req = urllib.request.Request(url)
#向请求体里添加User-Agent
req.add_header("User-Agent",agentStr)
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)












