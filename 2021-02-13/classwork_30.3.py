array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter elements"))
    array.append(elements)

for i in range(1,amount_elements,2):
    if array[i]%5 == 0:
        print(array[i])

