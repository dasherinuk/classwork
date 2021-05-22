array=[]
amount=int(input("Enter the amount of elements"))
for i in range(0,amount):
    elements=int(input("Enter an element"))
    array.append(elements)

sum1=0
for i in range(amount):
    sum1+=array[i]

print(sum1)
    
   

    
    
