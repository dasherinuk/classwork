array1=[]
array2=[]
for i in range(0,5):
    userinput1=input("Enter an element")
    array1.append(userinput1)

for i in range(0,5):
    userinput2=input("Enter an element")
    array2.append(userinput2)

array1_more=0
array2_more=0
for i in range(0,5):
    if array1[i]>array2[i]:
        array1_more=array1_more+1

    else:
        array2_more=array2_more+1

print(array1_more)
print(array2_more)

if array1_more>array2_more:
    print("array1_more")
else:
    print("array2_more")

        
