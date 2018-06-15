# -*- coding: utf-8 -*-
import urllib.request
import ssl
import json

def ajaxCrawler(url):
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    
    #使用ssl创建未验证的上下文
    context = ssl._create_unverified_context() 
    response = urllib.request.urlopen(req,context=context)
    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)
    return jsonData

    

# =============================================================================
# 
# url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=20"
# info = ajaxCrawler(url)
# print(info)
# 
# =============================================================================
for i in range(1,11):
    print(i)
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start="+str(i*20)
    info = ajaxCrawler(url)
    print(len(info))
    
    
