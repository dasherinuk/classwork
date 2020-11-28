array = [int(r) for r in input().split()]
array2 = [int(r) for r in input().split()]
# len_array=len(array)
# len_array2=len(array2)
# array3=[]
# for i in range(0,len_array):
#     array3.append(array[i])
# for p in range(0,len_array2):
#     array3.append(array2[p])
array3 = array + array2
print(array3)