p=int(input("Enter the point"))
x1=int(input("Enter x1 "))
x2=int(input("Enter x2"))

if x1==p:
    print("on left board")
elif x2==p:
    print("on right board")
elif p <= x2 and p >= x1:
    print("inside")
else:
    print("outside")

