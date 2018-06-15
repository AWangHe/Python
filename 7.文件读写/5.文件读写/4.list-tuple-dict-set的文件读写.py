# -*- coding: utf-8 -*-
import pickle    #数据持久性模块

myList = [1,2,3,4,5,"sunck is a good man"]
path = r"F:\Python\data\7.文件读写\5.文件读写\file05.txt"

#写入
f = open(path, "wb")
pickle.dump(myList, f)
f.close()


#读取
f1 = open(path, "rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()
























