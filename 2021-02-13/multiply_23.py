array=[]
for i in range(0,10):
    userinput=int(input("Enter element"))
    array.append(userinput)

multiply_sum=array[0]
for i in range(1,10):
    multiply_sum*=array[i]
print(multiply_sum)
