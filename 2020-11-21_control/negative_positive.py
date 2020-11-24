array=[int(k) for k in input("Enter your elements:").split()]
len_array=len(array)
for i in range(0,len_array):
    if array[i]<0:
        array[i]=array[i]*-1

print(array)