#1 2 3 4 5 6 2 8 1 3 9

array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)

for i in range(0,amount_elements):
    colision = False
    for j in range(0,amount_elements):
        if array[i]==array[j] and i!=j:
            colision = True

    if colision == True:
        print(array[i], "Is not unique")
    else:
        print(array[i],"Is unique")
        

