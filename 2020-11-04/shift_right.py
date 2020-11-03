array=[]
amount=int(input("Enter the amount of elements"))

for i in range (0,amount):
    element_input=int(input("Enter your element"))
    array.append(element_input)

print(array)

# 5 0 1 3 5
# 0 5 0 1 3

t = array[0]

for i in range(1, amount):
    temp = array[i]
    array[i] = t
    t = temp

array[0]=0
print(array)

