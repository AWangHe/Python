# -*- coding: utf-8 -*-
import sys
import importlib
importlib.reload(sys)
#pip install pdfminer3K
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams 
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed 

def func(str):
    print(str + "!")
def readPDF(path, callback=None, toPath=""):
    #以二进制形式打开PDF文件
    f = open(path, "rb")   
    #创建一个PDF文件分析器
    parser = PDFParser(f)   
    #创建PDF文档
    pdfFile = PDFDocument()
    #连接分析器与文档对象
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    #提供初始化代码
    pdfFile.initialize()
    
    #检测文档是否提供TXT转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed 
    else:
        #解析数据
        
        #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager, device)
        #开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            #图层
            layout = device.get_result()
            for x in layout:
                if(isinstance(x,LTTextBoxHorizontal)):
                    if toPath == "":
                        #处理每行数据
                        str = x.get_text()
                        if callback != None:
                            callback(str)
                        else:
                            print(str)
                    else:
                        #写文件
                        print("将PDF中读出的数据写入文件")
            


path = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\3.读取pdf文件\002.pdf"
readPDF(path, func)


















