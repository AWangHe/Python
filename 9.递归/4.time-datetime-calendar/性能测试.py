# -*- coding: utf-8 -*-
import time 

print(time.clock())
sum = 0
for i in range(100000000):
    sum += i

print(time.clock())