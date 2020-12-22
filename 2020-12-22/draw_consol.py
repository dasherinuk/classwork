array = []
size = 20
for i in range(size):
    array.append(['.']*size)

for i in range(size):
    array[i][0]='+'

for i in range(size):
    array[i][-1]='+'

for i in range(size):
    array[0][i]='+'

for i in range(size):
    array[-1][i]='+'

for i in range(size):
    array[i][i]='+'

for i in range(size):
    array[i][-i-1]='+'

for i in range(size):
    print(*array[i],sep='')

