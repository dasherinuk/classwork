array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter elements"))
    array.append(elements)

for i in range(0,amount_elements):
    if array[i]%7==0:#число делиться на 7 если остаток от деления на 7 равен 0
        print(array[i])
