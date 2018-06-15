# -*- coding: utf-8 -*-
from father import Father
from mother import Mother

class Child(Father, Mother):
    def __init__(self, money, faceValue):
        #注意写法
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)













