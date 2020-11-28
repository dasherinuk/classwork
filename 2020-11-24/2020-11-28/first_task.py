array = [int(r) for r in input().split()]
len_array=len(array)
array_odd=array[1::2]#array[start:finish:step]
array_even=array[0::2]
max_odd=max(array_odd)
min_even=min(array_even)
print(min_even)
print(max_odd)
