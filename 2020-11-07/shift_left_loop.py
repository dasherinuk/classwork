# 1 2 3 4 5 6
# 2 3 4 5 6 1

# 1 2 3 4 5 6
# 3 4 5 6 1 2

list_input = [ int(item.strip()) for item in input("Enter numbers: ").split(",") ]
shift_n = int(input("Enter count shift: "))

for i in range(shift_n):
    first = list_input[0]
    for i in range(len(list_input)-1):
        list_input[i]=list_input[i+1]
    list_input[-1] = first

print(*list_input, sep=", ")

