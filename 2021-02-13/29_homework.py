array=[]
even=0
odd=0
element_amount=int(input("Enter amount of elements"))

for i in range(0,element_amount):
    userinput=int(input("Enter element"))
    array.append(userinput)

len_array=len(array)
for i in range(0, len_array//2):
    print(array[2*i+1])#odd position
    
for i in range(0, len_array//2):
    even=(array[2*i])#even position
    print(even)
    

sum_even=0
for  i in range(0,len_array,2):
    sum_even+=array[i]
    
average_even=sum_even/len_array
print(average_even)

sum_odd=0
for  i in range(1,len_array, 2):
    sum_odd+=array[i]
    

average_odd=sum_odd/len_array
print(average_odd)

sum_of=0
for  i in range(0,len_array):
    sum_of+=array[i]


average=sum_of/len_array
print(average)

if average_odd>average and average_odd>average_even:
    print("Odd average is bigger")
elif average_even>average and average_even>odd_average:
    print("Even average is bigger")
else:
    print("Average is bigger")
    


