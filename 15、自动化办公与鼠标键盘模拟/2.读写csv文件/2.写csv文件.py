# -*- coding: utf-8 -*-
import csv
def writeCsv(path, data):
    with open(path, "w", encoding='utf-8') as f:
        writer = csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)
        
path = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\2.读写csv文件\002.csv"
data = [[1,2,3], [4,5,6], [7,8,9]]
writeCsv(path, data)





















    
