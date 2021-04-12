array=[]
for i in range (0,5):
    userinput=int(input("Enter an element"))

    array.append(userinput)

print(array)

# 1 2 3 4 5
# multiply = 1 
# multiply = multiply * 2  1*2
# multiply = multiply * 3  1*2*3
# multiply = multiply * 4  1*2*3*4
# multiply = multiply * 5  1*2*3*4*5
multiply=array[0]
for i in range(1,5):
    multiply=multiply*array[i]

print(multiply)


sum_array=array[0]
for i in range(1,5):
    sum_array=sum_array+array[i]

print(sum_array)

odd=0
even=0
for i in range(0,5):
    if array[i] %2 :
        odd=odd+1

    else:
        even=even+1

print(odd)
print(even)


negative=0
positive=0
zero=0
for i in range(0,5):
    if array[i]>0:
        positive=positive+1
    elif array[i]<0:
        negative=negative+1
    else:
        zero=zero+1

print(positive)
print(negative)
print(zero)
