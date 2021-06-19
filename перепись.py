array=[]
array_number=[]
number=int(input("Enter amount of people"))
for i in range(number):
    a,g = [int(item) for item in input().split()]
    if g==1:
        array.append(a)
        array_number.append(i+1)
max1=max(array)
ind = array.index(max1)
print(array_number[ind])
print(array)
print(array_number)
