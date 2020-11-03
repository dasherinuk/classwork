array=[]
amount=int(input("Enter the amount of elements"))

for i in range (0,amount):
    element_input=int(input("Enter your element"))
    array.append(element_input)

print(array)

# 5 0 1 3 5
# 0 5 0 1 3


for i in range(amount-1, 0, -1):# if ammount = 5 then i = 4 ... 1
    array[i] = array[i-1]

array[0]=0
print(array)

