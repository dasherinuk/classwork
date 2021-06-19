t_room, t_cond = [int(item) for item in input().split()]
change=input("Enter change")

if change=="freeze":
    print(min(t_room, t_cond ))
elif change=="heat":
    print(max(t_room, t_cond ))
elif change=="auto":
    print(t_cond)
else:
    print(t_room)
