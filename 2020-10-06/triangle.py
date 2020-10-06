from turtle import fd, lt,rt,goto,up,down
def draw_triangle(x,y,size=100, turn=lt):
    up()
    goto(x,y)
    down()
    fd(size)
    turn(120)
    fd(size)
    turn(120)
    fd(size)
    turn(120)

draw_triangle(y=50,x=100)
draw_triangle(size=50, turn = rt, y=0, x = 25)
#draw_triangle(rt)

