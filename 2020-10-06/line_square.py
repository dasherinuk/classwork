from turtle import *

def draw_square(size):
    fd(size)
    rt(90)
    fd(size)
    rt(90)
    fd(size)
    rt(90)
    fd(size)
    rt(90)#retur old state

def draw_triangle(size, turn):
    fd(size)
    turn(120)
    fd(size)
    turn(120)
    fd(size)
    turn(120)

def draw_triangle_down(size):
    draw_triangle(size, rt)

def draw_line(count, size, draw, offset=0):
    for i in range(count):
        draw(size)
        up()
        fd(offset+size)
        down()

#draw_line(3,30, lambda size: draw_triangle(size, lt))
#draw_line(3,30, draw_triangle_down)
#draw_line(3,30, draw_square)
draw_line(3,30, lambda size: circle(size//2))
