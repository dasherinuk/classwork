from turtle import *

def draw_D(x,y,size):
    up()#up pen
    goto(x,y)#go to coordinate x,y
    down()#down pen
    #draw letter D
    fd(size//2)#line bottom
    lt(45)#turn left 45
    fd(size)
    lt(90)
    fd(size)
    lt(45)
    fd(size//2)#line top
    goto(x,y)
    #beck turn
    lt(180)

