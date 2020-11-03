array=[]
amount=int(input("Enter the amount of elements"))

for i in range (0,amount):
    element_input=int(input("Enter your element"))
    array.append(element_input)

print(array)


for i in range(0, amount-1, 2):
    array[i],array[i+1] = array[i+1],array[i]

print(array)