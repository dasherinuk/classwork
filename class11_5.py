array=[0,1]

for i in range(20):
    array.append(array[-2]+array[-1])

print(array)
