array = []
size = 20
for i in range(size):
    array.append(['.']*size)

for j in range(0, 15, 5):
    for i in range(5):
        array[j+i][j+i]='+'
    
    for i in range(5):
        array[j+i][j+4-i]='+'


for i in range(size):
    print(*array[i],sep='')