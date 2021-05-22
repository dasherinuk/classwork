array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)

for i in range(0,amount_elements):
    colision = 1#!!!
    for j in range(0,amount_elements):#!!!
        if array[i]==array[j] and i!=j:
            colision = colision+1
    print(array[i],colision)

 

