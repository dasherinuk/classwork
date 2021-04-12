array=[]
amount_elements=int(input("Enter amount of elelemnts"))
for  i in range(0,amount_elements):
    element=int(input("Enter an element"))
    array.append(element)
elements_in_row=int(input("Enter elelemnts in row"))

while amount_elements!=elements_in_row:
    for j in range(elements_in_row):
        print(array[i])
        array[i]+=1
print(array[i])
        
#while amount_elements%elements_in_row!==


##
##for i in range(0,elements_in_row-elements_in_row%elements_in_row,elements_in_row):
##    for i in range(0,elements_in_row):
##        print(array[i])
##
##if amount_elements%elements_in_row == i:
##    print(array[-i])

