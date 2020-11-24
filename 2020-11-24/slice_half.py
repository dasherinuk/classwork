array = [int(r) for r in input().split()]
len_array=len(array)
half_len=len_array//2

left = array[0:half_len:]
right = array[half_len::]

print(left)
print(right)
