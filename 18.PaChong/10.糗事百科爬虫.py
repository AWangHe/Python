# -*- coding: utf-8 -*-
import urllib.request
import re

def jokeCrawler(url):
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    
    response = urllib.request.urlopen(req)
    HTML = response.read().decode("utf-8")
    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat,re.S)
    divsList = re_joke.findall(HTML)
#    print(divsList)
#    print(len(divsList))
    dic = {}
    for div in divsList:
        #用户名
        re_u = re.compile(r'<h2>(.*?)</h2>',re.S)
        username = re_u.findall(div)
        username = username[0]
#        print(username)
        #段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>',re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0]
#        print(duanzi)
        dic[username] = duanzi
    return dic
    
#    with open(r"F:\Python\data\PaChong\qiubai.html","w") as f:
#        f.write(HTML)

url = "https://www.qiushibaike.com/text/page/2/"
info = jokeCrawler(url)
#print(info)
for k,v in info.items():
    print(k + "讲段子\n" + v)
























