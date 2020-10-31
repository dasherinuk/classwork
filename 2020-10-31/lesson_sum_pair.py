list_numbers = []
amount_numbers = int(input())

for i in range(amount_numbers):
    list_numbers.append(int(input()))

print(list_numbers)

for i in range(amount_numbers-1):
    list_numbers[i] += list_numbers[i+1]

print(list_numbers)