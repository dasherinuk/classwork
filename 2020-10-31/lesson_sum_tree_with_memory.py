list_numbers = []
amount_numbers = int(input())

for i in range(amount_numbers):
    list_numbers.append(int(input()))

print(list_numbers)

prev = list_numbers[0]
for i in range(1,amount_numbers-1):
    t = list_numbers[i]
    list_numbers[i] += list_numbers[i+1] + prev
    prev =  t

print(list_numbers)

# 1 2 3 4 5
# 1 6 13 22 5 dont work
# 1 6 9 12 5 