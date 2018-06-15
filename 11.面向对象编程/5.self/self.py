# -*- coding: utf-8 -*-
'''
self 代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表那个对象

self.__class__   代表类名
'''



class Person(object):
    def run(self):
        print("run") 
        print(self.__class__)
        p = self.__class__("man", 18, 190, 60)
        print(p)
    def eat(self, food):
        print("eat " + food)
    #self不是关键字，换成其它的标识符也是可以的，但是帅的人都是用self
    def play(a):
        print("paly basketball")
    def say(self):
        print("Hello! My name is %s, I am %d years old." % (self.name, self.age))
    def __init__(self, name, age, height, weight):
        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight =weight
        
per1 = Person("sunck", 18, 170, 55)
per1.say()
per1.run()





























