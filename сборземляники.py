x,y,z= [int(item) for item in input().split()]


if z>y or z>x:
    print("Impossible")
else:
    print(x+y-z,"berries")
