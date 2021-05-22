##1 2 3 4 5 1 5 1 7 1 0 2
##
##1 0
##2 0
##3 0
##4 0
##5 0
##1 1
##5 1
##1 2
##7 0
##1 3
##0 0
##2 1

array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)

        
for i in range(0,amount_elements):
    colision = 0
    for j in range(0,i):#!!!
        if array[i]==array[j] and i!=j:
            colision = colision+1
    print(array[i],colision)

 


