array = [int(r) for r in input().split()]
array2 = [int(r) for r in input().split()]
array3 = [int(r) for r in input().split()]
all_array=[]
min1=min(array)
min2=min(array2)
min3=min(array3)
all_array=[min1,min2,min3]

print(min(all_array))
