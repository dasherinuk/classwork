array=[]
amount_elements=int(input("Enter amount of elements"))
for i in range(0,amount_elements):
    element=int(input("Enter an element"))
    array.append(element)

for i in range(0,amount_elements-amount_elements%4,4):
    print(array[i],array[i+1],array[i+2],array[i+3])

if amount_elements%4 == 1:
    print(array[-1])
if amount_elements%4 == 2:
    print(array[-2],array[-1])
if amount_elements%4== 3:
    print(array[-3],array[-2],array[-1])
