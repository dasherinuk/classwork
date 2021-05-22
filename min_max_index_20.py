array=[]
amount=int(input("Enter amount"))
for i in range(0,amount):
    userinput=int(input("Enter elements:"))
    array.append(userinput)

minimum=array[0]
maximum=array[0]
index_min=0
index_max=0

for i in range(0,amount):
    if array[i]>maximum:
        index_max = i
        maximum=array[i]
    if array[i]<minimum:
        index_min = i
        minimum=array[i]

print(minimum)
print(maximum)

for i in range(len(array)):
    print(array[len(array)-i-1],end=" ")

print()




