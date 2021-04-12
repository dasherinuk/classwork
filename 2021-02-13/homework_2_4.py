array=[]
userinput=int(input("Enter amount of elements"))

for i in range(0,userinput):
    userinput2=int(input("Enter element"))
    array.append(userinput2)

##len_array=len(array)
##for i in range(0,userinput):
##    if array[i]%2==0 and ### %2==0 :
##        print(array[i])
##    else:
##        array[i]%4==0:
##            print(array[i])
            
for i in range(0,userinput):
    #if i%2==0 and array[i]%2==0 or i%2!=0 and array[i]%4==0:
    #    print(array[i])
    if i%2==0:
        if array[i]%2==0:
             print(array[i])
    else:
        if array[i]%4==0:
             print(array[i])


#Можно elif в else??
