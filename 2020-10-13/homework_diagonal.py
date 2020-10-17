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

def draw_line(count, size, draw, offset=0):
    if count > 0:
        draw(size)
        up()
        fd(size+offset)
        rt(90)
        fd(size+offset)
        lt(90)
        #fd(offset+size)
        down()
        draw_line(count-1, size, draw, offset)

speed(0)
draw_line(5, 30, draw_fill_square)
input()

