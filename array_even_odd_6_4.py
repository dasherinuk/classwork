array=[]
array_even=[]
array_odd=[]

amount_elements=int(input("Enter amount"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)

for i in range(0,amount_elements):
    if array[i]%2==0:
        array_even.append(array[i])
    else:
        array_odd.append(array[i])

print(array_even)
print(array_odd)

len_array=len(array)
len_even=len(array_even)
len_odd=len(array_odd)
len_max = max(len_odd,len_even)

while len(array_even)<len_max:
    array_even.append(0)

while len(array_odd)<len_max:
    array_odd.append(0)

for i in range(0,len_max):
    sum_array=array_even[i]+array_odd[i]
    print(sum_array)
