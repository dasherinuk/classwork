a = 10
b = 20
arr=[10,20]

a,b = b,a

print(a,b)
print(arr)
i=0
arr[i],arr[i+1] = arr[i+1],arr[i]
#in the position of i ,is put in the position of i+1
print(arr)