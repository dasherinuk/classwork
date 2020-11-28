array = [int(r) for r in input().split()]
array2 = [int(r) for r in input().split()]
len_array=len(array)
len_array2=len(array2)
if len_array>len_array2:
    diff_len=len_array-len_array2
    for i in range(diff_len):
        array2.append(0)
else:
    len_diff=len_array2-len_array
    for i in range(len_diff):
        array.append(0)


array3=[]
for i in range(0,len_array):
    array3.append(array[i]+array2[i])

print(array3)




