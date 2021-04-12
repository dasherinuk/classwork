array=[]
amount_elements=int(input("Enter anount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)

for i in range(0,amount_elements-amount_elements%2,2):
    array[i],array[i+1]=array[i+1],array[i]

print(array)
