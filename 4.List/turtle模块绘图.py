# -*- coding: utf-8 -*-

'''
是一个简单的绘图工具

提供一个小海龟，可以把它理解为一个机器人，只能听得懂有限的命令
绘图窗口的原点(0,0)在正中间，默认海龟的方向是右侧

运动命令
forward(d)  向前移动d长度
backward(d)  向后移动d长度
right(d)     向右转动多少度
left(d)     向左转动多少度
goto(x,y)   移动到坐标为(x,y)的位置
speed(speed)  笔画绘制的速度[0,10]

笔画控制命令
up()   笔划抬起，在移动的时候不会绘图
down()  笔划落下，移动时会绘图
setheading(d)   改变海龟的朝向
pensize()    笔划的宽度
pencolor(colorstr)   笔划的颜色
reset()    回复所有设置，清空窗口，重置turtle状态
clear()     清空窗口，不会重置turtle
circle(r,e)  绘制一个圆形，r为半径，e为次数

begin_fill()          开始填充
fillcolor(colorstr)   填充颜色
end_fill()            结束填充

其它命令
done()  程序继续执行
undo()   撤销上一次动作
hideturtle()   隐藏海龟
showturtle()   显示海龟



'''
#导入turtle库
import turtle 

turtle.speed(1)
turtle.forward(100)
turtle.right(45)
turtle.forward(200)
turtle.goto(-100,-100)
turtle.up()
turtle.goto(-100,200)
turtle.down()
turtle.pensize(10)
turtle.pencolor("red")
turtle.forward(100)
turtle.circle(50)
turtle.goto(0,0)

turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(50,steps=5)
turtle.end_fill()


turtle.done()




















