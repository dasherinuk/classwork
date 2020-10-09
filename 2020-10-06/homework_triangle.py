from turtle import fd, lt,rt,goto,up,down
def draw_Triangle(x,y,size):
    up()#up pen
    goto(x,y)#go to coordinate x,y
    down()#down pen
    rt(60)
    fd(size)
    rt(60)
    fd(size)
    up()#up pen
    goto(x,y)#go to coordinate x,y
    down()#down pen
draw_Triangle

