array=[]
for i in range (0,10):
    userinput=int(input("Enter a number"))
    array.append(userinput)

                  
lenarray=len(array)
for i in range(0,lenarray):
    print(array[lenarray-i-1],end=" ")
