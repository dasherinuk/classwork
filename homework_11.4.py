array=[]
amount_elements=int(input("Enter amount of elelemnts"))
for  i in range(0,amount_elements):
    element=int(input("Enter an element"))
    array.append(element)
elements_in_row=int(input("Enter elelemnts in row"))

amount_row = amount_elements//elements_in_row
index = 0
for i in range(amount_row):
    for j in range(elements_in_row):
        print(array[index], end=" ")
        index+=1
    print()

for i in range(index, amount_elements):
    print(array[i], end=" ")

#its work
##for i in range(amount_elements):
##    if i!=0 and i % elements_in_row==0:
##        print()
##    print(array[i], end=" ")



