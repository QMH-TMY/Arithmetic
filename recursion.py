# -*- coding:UTF8 -*-
#!/usr/bin/python
#递归相关

###########################################################
def listsum(numlist):
    '''对列表数相加'''
    if 1 == len(numlist):
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])

#print(listsum([1,2,3,4,5,6]))


def convString(num=10,base=10):
    '''递归得到任意2-16进制的数字字符串'''
    convStr = "0123456789ABCDEF"
    if num < base:
        return convStr[num]
    else:
        return convString(num/base,base) + convStr[num%base]

#print(convString(1024,2))
###########################################################

import turtle
#myTurtle = turtle.Turtle()
#myWindow = turtle.Screen()
def drawSpiral(myTurtle,linLen):
    '''绕着画线条'''
    if linLen > 0:
        myTurtle.forward(90)
        myTurtle.right(45)
        drawSpiral(myTurtle,linLen-5)

#drawSpiral(myTurtle,100)
#myWindow.exitonclick()

###########################################################
def tree(branchLen,T):
    '''同构树'''
    if branchLen > 5:
        T.forward(branchLen)
        T.right(20)
        tree(branchLen-10,T)
        T.left(40)
        tree(branchLen-10,T)
        T.right(20)
        T.backward(branchLen)

def main():
    '''绘画'''
    T = turtle.Turtle()
    myWin = turtle.Screen()
    T.left(90)
    T.up()
    T.backward(100)
    T.down()
    T.color("green")
    tree(75,T)
    myWin.exitonclick()

#main()

##############################################################
def mainSierpinski():
    '''谢尔宾斯基三角形'''
    myTurtle = turtle.Turtle()
    myWindow = turtle.Screen()
    myPoints = [[-300,-50],[0,300],[300,-50]]

    sierpinski(myPoints,4,myTurtle)
    myWindow.exitonclick()
def drawTriangle(points,color,myTurtle):
    '''画三角形'''
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    '''取得中间坐标'''
    return((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(points,degree,myTurtle):
    '''找点上色'''
    colormap = ['blue','red','green','white','yellow','orange']

    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],getMid(points[0],points[1]),
                              getMid(points[0],points[2])],
                              degree-1,myTurtle)
        sierpinski([points[1],getMid(points[0],points[1]),
                              getMid(points[1],points[2])],
                              degree-1,myTurtle)
        sierpinski([points[2],getMid(points[2],points[1]),
                              getMid(points[0],points[2])],
                              degree-1,myTurtle)
#mainSierpinski()
##############################################################

def hannouta(Num):
    '''汉诺塔'''
    if Num == 1:
        return 1
    else:
        return hanouta(Num) + hanouta(Num-1)



