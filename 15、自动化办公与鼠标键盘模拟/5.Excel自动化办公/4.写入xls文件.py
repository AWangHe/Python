# -*- coding: utf-8 -*-
#有序字典
from collections import OrderedDict
#写入数据
from pyexcel_xls import save_data


def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetName, sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)
        
    save_data(path, dic)






path = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\5.Excel自动化办公\002.xls"
data = {'软件学院': [['姓名', '年龄', '班级', '学号'], ['王贺', 18, '三班', 123456], ['哈哈', 18, '四班', 123456]], '信息科学学院': [['姓名', '年龄', '班级', '学号'], ['啦啦啦', 18, '三班', 123456], ['哒哒哒', 18, '四班', 123456]]}
makeExcelFile(path, {'软件学院': [['姓名', '年龄', '班级', '学号'], ['王贺', 18, '三班', 123456], ['哈哈', 18, '四班', 123456]], '信息科学学院': [['姓名', '年龄', '班级', '学号'], ['啦啦啦', 18, '三班', 123456], ['哒哒哒', 18, '四班', 123456]]})































