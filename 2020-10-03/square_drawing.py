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

def draw_square_without_back(size):
    draw_square(size)
    lt(90)

size_square = 100
draw = draw_square_without_back


draw(size_square)


draw(size_square*1.5)


draw(size_square*2)


draw(size_square*2.5)
