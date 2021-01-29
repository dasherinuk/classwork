array = []
size = 20
for i in range(size):
    array.append(['.']*size*3)

# for i in range(0,20):
#     array[i][i//2]='+'
#     array[i][i]='+'
#     array[i][i*2]='+'
#     array[i][i*3]='+'
for i in range(0,20):
    array[i][i*3]='+'
    array[i][-i*3-1]='+'

for i in range(size):
    print(*array[i],sep='')


