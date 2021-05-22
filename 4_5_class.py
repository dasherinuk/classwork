#1 2 4 7 11 16 22
#+1
#+2
#+3
#+4
#+5
#+6

addition=1
for i in range(0,25,1):
    if i % 2 ==0:
        addition=addition+i
        print(i+1, addition)
    else:
        print(i+1, 0)
