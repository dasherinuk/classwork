array=[]

element_amount=int(input("Enter amount of elements"))

for i in range(0,element_amount):
    userinput=int(input("Enter element"))
    array.append(userinput)

len_array=len(array)
##for i in range(1,len_array,2):
##    print(array[i])

for i in range(0, len_array//2):
    print(array[2*i+1])#odd position
    
for i in range(0, len_array//2):
    print(array[2*i])#even position

sum_odd=0
for i in range(0,len_array//2):
    sum_odd+=array[2*i+1]
print(sum_odd)
    

multiply_even=1
for  i in range(0,len_array//2):
    multiply_even*=array[2*i]
print(multiply_even)

average=0
sum_of=0
for  i in range(0,len_array):
    sum_of+=array[i]
average=sum_of/len_array
print(average)
    
