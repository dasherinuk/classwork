from turtle import fd, lt,rt,goto,up,down
def draw_A(x,y,size):
    up()#up pen
    goto(x,y)#go to coordinate x,y
    down()#down pen
    lt(60)
    fd(size)
    rt(120)
    fd(size)
    lt(180)
    up()
    fd(size//2)
    down()
    lt(60)
    fd(size//2)
    lt(180)
    up()#up pen
    goto(x,y)#go to coordinate x,y
    down()#down pen

draw_A(100,100,50)
