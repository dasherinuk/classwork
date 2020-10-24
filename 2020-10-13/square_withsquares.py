from turtle import *

def draw_square(size, count = 8):
    if count >0:
        fd(size)
        rt(90)
        count=count-1
        draw_square(size,count=8)
def draw_line(count=8, size, draw, go_to_star, offset=0):
    go_to_star()
    for i in range(count):
        draw(size)
        up()
        fd(offset+size)
        down()
draw_line(count,size)     