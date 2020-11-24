array = [int(r) for r in input().split()]

for item in array[::]:
    if item %2 == 0:
        array.append(item)
        
print(array)