# -*- coding: utf-8 -*-
import csv
def readCsv(path):
    with open(path, "r", encoding='utf-8') as f:
        infoList = []
        allFileInfo = csv.reader(f)
        for row in allFileInfo:
            infoList.append(row)
    return infoList





path = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\2.读写csv文件\001.csv"
info = readCsv(path)



















