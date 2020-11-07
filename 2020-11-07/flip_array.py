array = [ int(item.strip()) for item in input("Enter numbers: ").split(" ") ]


# 1 2 3 4 5 6 input

# 6 2 3 4 5 1  #step 1
# 6 5 3 4 2 1  #step 2
# 6 5 4 3 2 1  #step 3

#[1, 2, 3, 4, 5, 6]
for i in range(0,len(array)//2): # i = 0, 1, 2
    left = i                     # 0, 1, 2
    right = len(array) - 1 - i   # 5, 4, 3
    array[left],array[right]=array[right],array[left]

print(array)

    
