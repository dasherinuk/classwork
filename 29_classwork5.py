one,two,three = [int(item) for item in input().split()] # 1 2 3 4 


if one + two==three:
    print("True")
elif one + three==two:
    print("True")
elif two+three==one:
    print("True")
else:
    print("False")
