from turtle import *

def draw_square(size, count = 4):
    if count >0:
        fd(size)
        rt(90)
        count=count-1
        draw_square(size,count)


def draw_triangle(size,count=3):
    if count >0:
        fd(size)
        lt(120)
        count=count-1
        draw_triangle(size,count)

def draw_cross(size,count=4):
    if count >0:
        draw_square(size//3)
        fd(size//3)
        lt(90)
        count=count-1
        draw_cross(size,count)

def draw_tri(size,count=4):
    if count >0:
        draw_triangle(size)
        fd(size)
        rt(90)
        count=count-1
        draw_tri(size,count)

        
draw_tri(100)       
# draw_cross(100)
# draw_square(100)
# draw_triangle(100)
input()