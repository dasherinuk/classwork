amount, number = [int(item) for item in input().split()]

page = number//amount
line = number%amount

if line == 0:
    line = amount
else:
    page +=1

print(page, line)
