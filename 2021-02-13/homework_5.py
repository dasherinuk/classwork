array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)

for i in range(0,amount_elements-amount_elements%2,2):
    array[i],array[i+1]=array[i+1],array[i]
    #if len(array)%2!=2:
        #array.append(0)

lenby2=len(array)%2
for i in range(0,amount_elements-amount_elements%2,2):
    if lenby2 %2!=2:
        array.append(0)

print(array)
