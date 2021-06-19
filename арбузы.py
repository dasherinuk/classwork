array=[]
amount=int(input("Enter amount of watermelon"))
for i in range(amount):
    weight=int(input("Enter weight of watermelon"))
    array.append(weight)
print(max(array),"for you")
print(min(array),"as present")
