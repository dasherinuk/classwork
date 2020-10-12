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

def draw_fill_square(size):
    begin_fill()
    draw_square(size)
    end_fill()

def draw_line(count, size, draw, go_to_star, offset=0):
    go_to_star()
    for i in range(count):
        draw(size)
        up()
        fd(offset+size)
        down()

def empty():
    pass

def jump(x,y):
    up()
    goto(x,y)
    down()
#lt(90)
speed(0)
draw_line(4,30, draw_fill_square, go_to_star=empty, offset=30)
jump(30,30)
draw_line(4,30, draw_fill_square, go_to_star=empty, offset=30)
jump(0,60)
draw_line(4,30, draw_fill_square, go_to_star=empty, offset=30)
jump(30,90)
draw_line(4,30, draw_fill_square, go_to_star=empty, offset=30)
jump(0,120)
draw_line(4,30, draw_fill_square, go_to_star=empty, offset=30)
jump(30,150)
draw_line(4,30, draw_fill_square, go_to_star=empty, offset=30)
jump(0,180)
draw_line(4,30, draw_fill_square, go_to_star=empty, offset=30)
jump(30,210)
draw_line(4,30, draw_fill_square, go_to_star=empty, offset=30)




