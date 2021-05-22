#0 1 1 2 3 5 8 13 21 34 55 ...
#0 1 1 2 4 7 13 24 44 ....
a = 0
b = 1
for i in range(20):
    print(a)
    c = a + b
    a = b
    b = c

