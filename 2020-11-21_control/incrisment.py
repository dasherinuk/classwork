array=[int(k) for k in input("Enter your elements:").split()]#[int(h) for k in input("Enter your elements:").split()]
len_array=len(array)
for i in range(0,len_array):#len_array-1
    array[i]=array[i]+1#array[i]=array[i+1]

print(array)