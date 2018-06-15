# -*- coding: utf-8 -*-
from cat import Cat
from mouse import Mouse
from person import Person
'''
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物


'''

tom = Cat("tom")
jerry = Mouse("jerry")


tom.eat()
jerry.eat()

#思考：再添加100种动物，也都有name属性和eat方法
#定义一个有name属性和eat方法的Animal类，让所有的动物类都继承自Animal
per = Person()
#per.feedCat(tom)
#per.feedMouse(jerry)


#思考：人要喂100种动物，难道要写100种feed方法吗？
#tom 和 jerry  都继承自动物
per.feedAnimal(tom)
per.feedAnimal(jerry)


















