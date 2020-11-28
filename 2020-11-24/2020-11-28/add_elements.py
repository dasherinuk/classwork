array = [int(r) for r in input().split()]
array2 = [int(r) for r in input().split()]
len_array=len(array)
array3=[]
for i in range(0,len_array):
    array3.append(array[i]+array2[i])

print(array3)

