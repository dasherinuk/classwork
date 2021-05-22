x1=int(input("left "))
y1=int(input("top "))

x2=int(input("right "))
y2=int(input("bottom "))


px=int(input("Enter x "))
py=int(input("Enter y "))


if px<=x2 and px >=x1:
    if py >=y2 and py <=y1:
        print("inside")
    else:
        print("outside")
else:
    print("outside")

