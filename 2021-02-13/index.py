n = 10
for i in range(0,n):
    print(i, end=" ")


print()

for i in range(0,n):
    print(n-i, end=" ")


print()

for i in range(0,n):
    print(n-i-1, end=" ")

print()

for i in range(0,n):
    print((i, n-i-1), end=" ")


print()
print()
print("work with list")

list_digit = [i*10 for i in range(1,11)]

for i in range(len(list_digit)):
    print(list_digit[i],end=" ")

print()
for i in range(len(list_digit)):
    print(list_digit[len(list_digit)-i-1],end=" ")



