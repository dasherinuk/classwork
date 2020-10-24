list_numbers = [ 1, 8, 2, 6, 4, 0]
               # 0  1  2  3  4  5
               #-6 -5 -4 -3 -2 -1

print(list_numbers)
print(list_numbers[0])
print(list_numbers[3])
print(list_numbers[3] + list_numbers[0])
print(list_numbers)

list_numbers[0] = sum(list_numbers)
print(list_numbers)
list_numbers.append(10)
print(list_numbers)
list_numbers.sort()
print(list_numbers)
print(list_numbers[-1])
print(len(list_numbers))