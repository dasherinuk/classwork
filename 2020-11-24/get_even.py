array = [int(r) for r in input().split()]
array2=[]
len_array=len(array)

for i in range(2,len_array,2):
    array2.append(array[i])


print(array2)