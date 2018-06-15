# -*- coding: utf-8 -*-
def outer(func):
    def inner(*args,**kwargs):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$")
        func(*args,**kwargs)
    return inner
  
#函数的参数个数理论上是无限制的，但实际上最好不要超过6,7个
@outer
def say(name,age):
    print("My name is %s , I am %d years old." % (name,age))

say("sunck",18)































