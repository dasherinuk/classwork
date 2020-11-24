#read the array of the user and split it in half,left side is 1 right is 2
#1234 left=12 right=34

array = [int(r) for r in input().split()]
left=[]
right=[]
len_array=len(array)
half_len=len_array//2

for i in range(0,half_len):
    left.append(array[i])

for h in range(half_len,len_array):
    right.append(array[h])

print(left)
print(right)
