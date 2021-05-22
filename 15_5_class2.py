array=[]
amount=int(input("Enter amount of elements"))
for i in range(amount):
    elements=int(input("Enter an element"))
    array.append(elements)
    
odd=0
even=0
for i in range(amount):
    if array[i]%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)
