array = []
size = 20
for i in range(size):
    array.append(['.']*size)

for i in range(5):
    for ind in range(5):
        array[i][ind]='+'



for i in range(size):
    print(*array[i],sep='')

