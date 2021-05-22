array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter elements:"))
    array.append(elements)

for i in range(amount_elements-1,-1,-1):
    if i % 2 == 0 and array[i]%2==0:
        print(array[i])
    
