# -*- coding: utf-8 -*-
import os

'''
os:包含了普遍的操作系统的功能

'''
#获取操作系统的类型， nt->windows   posix->Linux、Unix 或者 Mac OS X
#print(os.name)

#打印操作系统详细的信息（注意Windows不支持）
#print(os.uname())

#获取操作系统中的所有环境变量
#print(os.environ)
#获取指定环境变量
#print(os.environ.get("JAVA_HOME"))

#获取当前目录  ./a/
#print(os.curdir)

#获取当前工作目录，即当前Python脚本所在的目录
#print(os.getcwd())

#以列表的形式返回指定目录下的所有文件
#print(os.listdir(r"D:\迅雷下载\电影"))


#在当前目录下创建新目录
#os.mkdir("sunck")

#在当前目录下删除目录
#os.rmdir("sunck")

#获取文件属性
#print(os.stat("2.os模块.py"))

#重命名
#os.rename("sunck","hue")

#删除普通文件
#os.remove("01.txt")

#运行shell命令
#os.system("notepad")
#os.system("write")
#os.system("mspaint")
#os.system("msconfig")
#os.system("shutdown -s -t 500")
#os.system("shutdown -a")
#os.system("taskkill /f /im notepad.exe")


#有些方法存放os模块里，还有些存放在os.path里
#查看当前的绝对路径
#print(os.path.abspath("."))

#拼接路径
#p1 = "D:\\迅雷下载\\电影\\"
#p2 = "sunck\abc\d"
#注意：参数二开始不要有斜杠

#join()方法通用
#p3 = "/root/he/haha"
#p4 = "sunck"
#print(os.path.join(p3, p4))

#拆分路径
path2 = "F:\Python\data\8.os模块\adc.txt"
#print(os.path.split(path2))

#获取扩展名,若果没有扩展名返回空
#print(os.path.splitext(path2))

#判断是否是目录
#print(os.path.isdir(path2))

#判断文件是否存在
path3 = r"F:\Python\data\8.os模块\2.os模块.py"
#print(os.path.isfile(path3))

#判断目录是否存在
path4 = r"F:\Python\data\8.os模块"
#print(os.path.exists(path4))

#获得文件大小(字节)
#print(os.path.getsize(path3))


#获取文件的路径名
#print(os.path.dirname(path3))

#获取文件的名字
print(os.path.basename(path3))






























