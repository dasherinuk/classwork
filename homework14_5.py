# 5
# 100
# 120
# 50
# 30
# 200

#1: 100
#2: 220 100+120
#3: 270 100+120+50
#4: 300 100+120+50+30
#5: 500 100+120+50+30+200

rounds=int(input("Enter amounts of rounds"))

array=[]
for i in range(rounds):
    amount=int(input("How much do you get for round"))
    array.append(amount)

sum1=0
for i in range(rounds):
    sum1+=array[i]
    print("round ", i+1, ":", sum1)


# i = 0 1 2 3 4 5
# i+1 = 1 2 3 4 5 6
    

