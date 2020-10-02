from turtle import fd, lt,rt,goto,up,down

def draw_S(x,y,size):
    up()
    down()
    lt(90)
    fd(size)
    lt(90)
    fd(size)
    rt(90)
    fd(size)
    rt(90)
    fd(size)
    up()
    goto(x,y)
    down()
draw_S(100,100,50)

draw_S(0,0,25)
