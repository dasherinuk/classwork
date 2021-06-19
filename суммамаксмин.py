array=[]
oddar=[]
evar =[]
amount=int(input("Enter amount"))
for i in range (amount):
    numbers=int(input("Enter number"))
array.append(numbers)

if array[i]%2==0:
    evar.append(array[i])

else:
    Oddar.append(array[i])

print(max(evar)-min(oddar))

max1=max(oddar)
min1=min(evar)
print(max1-min1)
