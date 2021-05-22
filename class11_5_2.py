array=[]
amount=int(input("Enter amount of elements"))

for i in range(amount):
    elements=int(input("Enter an element"))
    array.append(elements)

mult=1
for i in range(elements):
    mult*=array[i]
print(mult)
