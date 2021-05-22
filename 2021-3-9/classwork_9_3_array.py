array=[]
array1=[]
array2=[]
for i in range(0,3):
    userinput=int(input("Enter a number"))
    array.append(userinput)

for j in range(0,3):
    userinput1=int(input("Enter a number"))
    array1.append(userinput1)

for n in range(0,3):
    userinput2=int(input("Enter a number"))
    array2.append(userinput2)




for i in range(len(array)):
    print(array[len(array)-i-1],end=" ")

print()

    
array,array2=array2,array        #first and last



    

array[0],array[len(array)-1]=array[len(array)-1],array[0]
array1[0],array1[len(array1)-1]=array1[len(array1)-1],array1[0]
array2[0],array2[len(array2)-1]=array2[len(array2)-1],array2[0]

print(array)
print(array1)
print(array2)
