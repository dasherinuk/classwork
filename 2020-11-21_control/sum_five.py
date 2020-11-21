# 1 2 3 4  5 6 7 8 9  0
# 1 2 3 4 15 6 7 8 9 30
#is too hard
array=[int(k) for k in input("Enter your elements:").split()]
len_array=len(array)
for i in range(4,len_array,5):
    sum_five = 0
    for j in range(i-4,i+1):
        sum_five += array[j]
    array[i]=sum_five

print(array)