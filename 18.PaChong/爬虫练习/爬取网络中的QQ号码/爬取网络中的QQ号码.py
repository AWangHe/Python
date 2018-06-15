# -*- coding: utf-8 -*-
import urllib.request
from urllib.error import URLError, HTTPError
import ssl 
import os
import re 
from collections import deque


def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb")  as f:
        f.write(htmlBytes)
        
def writeFileStr(htmlBytes, toPath):
    with open(toPath, "w")  as f:
        f.write(str(htmlBytes))

def getHtmlBytes(url):
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    try:    
        req = urllib.request.Request(url, headers=headers)
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(req, context=context)
        return response.read()
    except URLError as e:
        print('URLError!!!')
    except HTTPError as e:
		   print('HTTPError!!!')
        
def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    htmlStr = str(htmlBytes)
    
    #爬取网址
    pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    #去重
    urlsList = list(set(urlsList))
    
    #爬取QQ号码
    pat = r"[1,9]\d{4,9}"
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    #去重
    qqsList = list(set(qqsList))
    f = open(toPath, "a")
    for qqStr in qqsList:
        f.write(qqStr+"\n")
    f.close()
    
    return urlsList
        

def center(url, toPath):
    queue = deque()
    queue.append(url)
    
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlsList = qqCrawler(targetUrl, toPath)
        for item in urlsList:
            tempUrl = item[0]
            queue.append(tempUrl)

url = r"https://www.douban.com/group/topic/17359302/"
toPath = r"F:\Python\data\18.PaChong\爬虫练习\爬取网络中的QQ号码\qq.txt"
center(url, toPath)
























'''
(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}
\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)
'''
























