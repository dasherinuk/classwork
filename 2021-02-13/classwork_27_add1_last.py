array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    userinput=int(input("Enter element"))
    array.append(userinput)

for i in range(0,amount_elements//2):
    print(array[i]+array[amount_elements-i-1])
