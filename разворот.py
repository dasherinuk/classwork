array=[]
for i in range(3):
    userinput=int(input("Enter a number"))
    array.append(userinput)

array[0],array[2]=array[2],array[0]
print(array)

