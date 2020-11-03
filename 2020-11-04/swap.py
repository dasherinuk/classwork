# 1 2 3 4 8 6 7 8 9
# 3 2 1 4 8 6 9 8 7

array=[]
amount=int(input("Enter the amount of elements"))

for i in range (0,amount):
    element_input=int(input("Enter your element"))
    array.append(element_input)

for i in range(0,amount-2,3):
    if array[i]<array[i+1] and array[i+1]<array[i+2]:
        #array[i],array[i+1],array[i+2]=array[i+2],array[i+1],array[i]
        array[i],array[i+2]=array[i+2],array[i]
print(array)