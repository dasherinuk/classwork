array=[]
userinput=int(input("Enter amount of elements"))

for i in range(0,userinput):
    userinput2=int(input("Enter element"))
    array.append(userinput2)

for i in range(0,userinput,4):
    print(array[i])
