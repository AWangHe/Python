# -*- coding: utf-8 -*-

class Person(object):
    name = ""
    age = 0
    height = 0
    weight = 0
    
    def run(self):
        print("run")        
    def eat(self, food):
        print("eat " + food)
    def openDoor(self):
        print("我已经打开了冰箱门。")
    def fillEle(self):
        print("我把大象装进了冰箱。")
    def closeDoor(self):
        print("我关闭了冰箱门。")
        
per = Person()

'''
访问属性：
格式：对象名.属性名
赋值： 对象名.属性名 = 新值

'''
  
per.name = "sunck"
per.age = 18
per.height = 180
per.weight = 70
print(per.name, per.age, per.height, per.weight)      
        
        
'''
访问方法：
格式：对象名.方法名(参数列表)
'''        
per.openDoor()
per.fillEle()
per.closeDoor()
        
per.eat("apple")       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        