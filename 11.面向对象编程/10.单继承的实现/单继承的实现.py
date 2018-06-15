# -*- coding: utf-8 -*-
from student import Student
from worker import Worker

stu = Student("sunck", 18, 123456, 1011)
print(stu.name, stu.age)
stu.run()
print(stu.stuId)
print(stu.getMoney())  #通过继承过来的公有方法访问私有属性
#print(stu.__money)    #私有属性
#stu.stuFunc()

wor = Worker("lilei", 21, 100)
print(wor.name, wor.age)
stu.eat("apple")



























