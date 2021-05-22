array=[]
amount=int(input("Enter amount of elements"))

for i in range(amount):
    elements=int(input("Enter an element"))
    array.append(elements)
    
max1=array[0]
min1=array[0]
for i in range(amount):
    if array[i]>max1:
        max1=array[i]
    if array[i]<min1:
        min1=array[i]

print(min1)
print(max1)
    
