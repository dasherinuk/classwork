array = [0,1,2,3,4,5,6,7,8,9,]
array2=[]

print (array)

for i in range(len(array)):
    print(array[len(array)-i-1],end=" ")
    array2.append(array[len(array)-i-1])
print ()


print (array2)
