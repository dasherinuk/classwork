array=[int(k) for k in input("Enter your elements:").split()]
len_array=len(array)
for i in range(0,len_array):
    array[i]=array[i]*array[i]
print(array)