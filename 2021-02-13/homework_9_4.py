array=[]
arr_pairs=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)

#разбиваем массив на пары сохраняем  все пары в один обший массив пар

for i in range(0,amount_elements-amount_elements%2, 2):
    arr_pairs.append([array[i],array[i+1]])
    
if len(array)%2!=0:
    arr_pairs.append([array[-1], 0])

#если пар не четное количество то добавляем новую пару из двух нулей
if len(arr_pairs)%2!=0:
    arr_pairs.append([0,0])

print(arr_pairs)
##1 пара это один индекс?
        
#переставляем пары метсами так как быдто это обычный массив
for i in range(0,len(arr_pairs), 2):
    arr_pairs[i],arr_pairs[i+1]=arr_pairs[i+1],arr_pairs[i]



#4 объединяем пары кодом выше в единный массив
arr_changed = []
for pair in arr_pairs:
    arr_changed.append(pair[0])
    arr_changed.append(pair[1])
print(arr_changed)
