# 1 2 3 4 5 6 7 8 9
# 1 2 3
# 4 5 6
# 7 8 9

array=[]
amount_elements=int(input("Enter amount of elelemnts"))
for  i in range(0,amount_elements):
    element=int(input("Enter an element"))
    array.append(element)

for i in range(0,amount_elements-amount_elements%3,3):
    print(array[i],array[i+1],array[i+2])

if amount_elements%3 == 1:
    print(array[-1])
if amount_elements%3 == 2:
    print(array[-2], array[-1])
