# -*- coding: utf-8 -*-


def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner


#使用@符号将装饰器应用到函数
@outer   #相当于say = outer(say)
def say(age):
    print("sunck is %d years old" % (age))


say(-10)





























