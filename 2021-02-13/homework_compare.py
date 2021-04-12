array1=[]
array2=[]
size = 5

for i in range(size):
    userinput=int(input("Enter an element"))
    array1.append(userinput)

for i in range(size):
    userinput1=int(input("Enter an element"))
    array2.append(userinput1)

for i in range(size):
    if array1[i]==array2[size-i-1]:
        i=i+1

if i == size:
    print("equals")
else:
    print("not equals")
