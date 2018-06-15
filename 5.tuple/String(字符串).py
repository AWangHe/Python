# -*- coding: utf-8 -*-

#split(str="",num)
#以str为分隔符截取字符串，指定num，仅截取num个字符串
str38 = "sucnk*is***a***good****man"
#print(str38.split("*",3))
#求单词的个数
list39 = str38.split("*")
c = 0
for s in list39:
    if len(s) > 0:
        c += 1
print(c)


#splitlines([keepends])   按照('\r','\r\n','\n')分隔
#keepends == True   会保留换行符
str40 = ''' sunck is a good man
sunck is a nice man
sunck is a handsome man 
'''
print(str40.splitlines())


#join(seq) 以指定的字符串分隔符，将seq中的所有元素组合成一个字符串
list41 =  ['sucnk','is','a','good','man']
list42 = " ".join(list41)
print(list42)

 
#max()  min()
str43 = "sunck is a good man z"
print("*"+max(str43)+"*")
print("*"+min(str43)+"*")


#replace(oldstr,newstr,count)  
#用newstr替换oldstr,默认是全部替换。如果指定了count，那么只替换前count个。
str44 = "sunck is a good good good man "
str45 = str44.replace("good","nice",1)
print(str44)
print(str45)


#创建一个字符串映射表
print("***************")
#       要转换的字符串    目标字符串
t46 = str.maketrans("ac","56")
# a---5   c---6
str47 = "sunck is a good man "
str48 = str47.translate(t46)
print(str48)


#startswith(str, start=0,end=len(str))
#在给定的范围内判断是否以给定的字符串开头，如果没有指定范围，默认是整个字符串
str49 = "sunck is a good man "
print(str49.startswith("sunck"))


#endswith(str, start=0,end=len(str))
#在给定的范围内判断是否以给定的字符串结尾，如果没有指定范围，默认是整个字符串
str50 = "sunck is a good man "
print(str50.endswith("man"))


#编码
#encode(encoding="utf-8",errors="strict")
str51 = "sunck is a good man "
#ignore   错误忽略
data52 = str51.encode("utf-8","ignore")
print(data52)


#解码   注意：要与编码时的编码格式一致
str53 = data52.decode("utf-8","ignore")
print(str53)


#isalpha()
#如果字符串中至少有一个字符且所有的字符都是字母返回True，否则返回False
str54 = "sunck is a good man "
print(str54.isalpha())


#isalnum()
#如果字符串中至少有一个字符且所有的字符都是字母或数字返回True，否则返回False
str55 = "123456"
print(str55.isalnum())


#isupper()
#如果字符串中至少有一个英文字符且所有的英文字符都是大写的英文字母返回True，否则返回False
print("ABC".isupper())
print("ABC#a".isupper())
print("ABC1".isupper())
print("ABC#".isupper())


#islower()
#如果字符串中至少有一个英文字符且所有的英文字符都是小写的英文字母返回True，否则返回False
print("abc".islower())
print("abcA".islower())
print("abc1".islower())
print("abc#".islower())

      
      
#istitle()
#如果字符串是标题化的返回True，否则返回FALSE
print("Sunck Is A Good Man".istitle())
print("sunck is".istitle())
print("sunck".istitle())      



#isdigit()
#如果字符串中只包含数字字符返回True，否则返回FALSE
print("123".isdigit())
print("123a".isdigit())



#isnumeric()  同上
#如果字符串中只包含数字字符返回True，否则返回FALSE
print("123".isnumeric())
print("123a".isnumeric())



#isdecimal()
#如果字符串中只包含十进制字符返回True，否则返回FALSE
print("123".isdecimal())
print("123a".isdecimal())


#isspace()
#如果字符串中只包含空格返回true，否则返回FALSE
print(" ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())


























































