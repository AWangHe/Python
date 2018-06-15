# -*- coding: utf-8 -*-
path = r"F:\Python\data\7.文件读写\5.文件读写\file04.txt"
with open(path, "wb") as f1:
    str = "sunck is a good man "
    f1.write(str.encode("utf-8"))


with open(path,"rb") as f2:
    data = f2.read()
    print(type(data))
    print(data)
    newData = data.decode("utf-8")
    print(type(newData))
    print(newData)






























