array=[]
Amount_input=int(input("Enter the amount of elements"))

for i in range (0,Amount_input):
    element_input=int(input("Enter your element"))
    array.append(element_input)
for i in range (len(array)):
    if i%2==0:
        array[i]+=1
    else:
        array[i]-=1

print(array)