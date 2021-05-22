#1 2 9 4 7 5 1 4 0 10 3 9
#1 9
#1 9
#0 10
#7 3

array=[]
amount_elements=int(input("Enter amount of elements"))

for i in range(0,amount_elements):
    elements=int(input("Enter an element"))
    array.append(elements)

amount_pairs=0
for i in range(0,amount_elements):
    for j in range(i+1,amount_elements):
        if array[i]+array[j]==10:
            amount_pairs=amount_pairs+1

print(amount_pairs)
        

