n = int(input("Enter the number"))
array=[1,n]

for i in range(2,n):
    if n%i==0:
        array.append(i)

print(array)
print(sum(array))
   
