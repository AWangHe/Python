# -*- coding: utf-8 -*-
import urllib.request
import re
import os

def imageCrawler(url, toPath):
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")
#    path = r"F:\Python\data\18.PaChong\爬虫练习\yhd.html"
#    with open(path, "wb") as f:
#        f.write(HtmlStr)
        
    pat = r'<img original="//(.*?)" />'
    re_image = re.compile(pat, re.S)
    imagesList = re_image.findall(HtmlStr)
#    print(imagesList)
#    print(len(imagesList))
    num = 1
    for imageUrl in imagesList:
        path = os.path.join(toPath, str(num)+".jpg")
        #print(path)
        num += 1
        #把图片下载到本地
        urllib.request.urlretrieve("http://"+imageUrl, filename=path)
        
    


url = r"http://search.yhd.com/c0-0/mbname-b/a35609::2880-s1-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E5%A5%B3%E8%A3%85/"
toPath = r"F:\Python\data\18.PaChong\爬虫练习\image"
imageCrawler(url, toPath)

















