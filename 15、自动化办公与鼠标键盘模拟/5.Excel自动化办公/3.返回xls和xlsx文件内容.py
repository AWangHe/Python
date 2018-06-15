# -*- coding: utf-8 -*-
'''
需要安装的包
pip  install xlrd
pip install future
pip install xlwt-future
pip install pyexcel-io
pip install ordereddict
pip install pyexcel
pip install pyexcel-xls
'''
#有序字典
from collections import OrderedDict
#读取数据
from pyexcel_xls import get_data

def readXlsAndXlsxFile(path):
    dic = OrderedDict()
    #抓取数据
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic
    
    

path = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\5.Excel自动化办公\001.xls"
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))



















