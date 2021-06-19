w,h,r = [int(item) for item in input().split()]
d=r*2
if w>=d and h>=d:
    print("Yes")
else:
    print("No")
