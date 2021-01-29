array = []
size = 20
for i in range(size):
    array.append([' ']*size)



for j in range(0, 15, 5):
    for row in range(5):
        for col in range(5):
            array[j+row][j+col]='+'
        
    
    #for i in range(5):
        #array[j+4][i+j]='+'


for i in range(size):
    print(*array[i],sep='')