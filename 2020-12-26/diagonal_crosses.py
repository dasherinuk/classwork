array = []
size = 30
for i in range(size):
    array.append(['.']*size)

for j in range(0, 15, 5):
    for i in range(5):
        array[i+j][j+2]='+'
    
    for i in range(5):
        array[j+2][i+j]='+'


*
*
*
*
*****






for i in range(size):
    print(*array[i],sep='')

