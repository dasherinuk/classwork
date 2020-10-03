from turtle import fd, lt,rt,up,goto,down

def draw_H(x,y,size):
    up()#up pen
    goto(x,y)#go to coordinate x,y
    down()#down pen
    lt(90)
    fd(size)
    rt(180)
    fd(size//2)
    lt(90)
    fd(size//2)
    lt(90)
    fd(size//2)
    rt(180)
    fd(size)
    lt(90)
    up()#up pen
    goto(x,y)#go to coordinate x,y
    down()#down pen



