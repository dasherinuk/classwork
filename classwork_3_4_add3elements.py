array=[]
array2=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)


for i in range(0,amount_elements-amount_elements%3,3):
    sum_3=array[i]+array[i+1]+array[i+2]
    array2.append(sum_3)

if amount_elements%3==1:# проверяем сколько элементов в последней тройке 
    array2.append(array[-1])#если остато от деленеия равен 1 то всего один элемент
elif amount_elements%3==2:
    array2.append(array[-1]+array[-2])

print(array)
print(array2)
    
    
