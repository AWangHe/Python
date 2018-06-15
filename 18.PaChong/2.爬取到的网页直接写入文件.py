# -*- coding: utf-8 -*-
import urllib.request

urllib.request.urlretrieve("http://www.baidu.com", 
                           filename = r"F:\Python\Test\file02.html")

#urlretrieve  在执行过程中会产生一些缓存
#清除缓存
#urllib.request.urlcleanup()

