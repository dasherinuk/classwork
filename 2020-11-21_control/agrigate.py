# 1 2 3  4  5  6  7  8  9
# 1 3 6 10 15 21 28 36 45

array=[int(k) for k in input("Enter your elements:").split()]
len_array=len(array)
for i in range(1,len_array):
    array[i]=array[i-1] + array[i]

print(array)

