from turtle import fd, lt,rt,goto,up,down

def draw_S(x,y,size):
    up()
    goto(x,y)
    down()
    fd(size)
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

    

