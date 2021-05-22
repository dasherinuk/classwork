array = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        userinput=int(input("Enter a number"))
        array[i].append(userinput)

for i in range(0,3):
    print(array[i])




array[0],array[2]=array[2],array[0]

for increase in range(0,3):
    array[increase][0],array[increase][2]=array[increase][2],array[increase][0]


