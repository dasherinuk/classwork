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

speed(0)

def draw_board(size, size_board):
    x,y = position()
    for index in range(size_board):
        jump(x+size*(index%2),y+size*index)
        draw_line(size_board//2+(index%2==0),size, draw_fill_square, go_to_star=empty, offset=size)
    

goto(50,50)
draw_board(20, 3)
goto(-200,0)
draw_board(20, 3)


