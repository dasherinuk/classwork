from turtle import *

def draw_square(size, count = 4):
    if count >0:
        fd(size)
        rt(90)
        count=count-1
        draw_square(size,count)


def draw_line(size, draw, count = 8, offset=0):
    if count>0:
        draw(size)
        up()
        fd(offset+size)
        down()
        draw_line(size, draw, count-1, offset)


def draw_multy_squeare(size, draw_row, count_row=8, count_col=8):
    if count_row>0:
        draw_row(size, count_col)
        up()
        fd(-size*count_col)
        lt(90)
        fd(size)
        rt(90)
        down()
        draw_multy_squeare(size, draw_row, count_row-1, count_col)


def def_line_suare(size, count):
    draw_line(size, draw_square, count)


lambda_line_squere = lambda size, count : draw_line(size, draw_square, count)

draw_multy_squeare(30, lambda_line_squere)
