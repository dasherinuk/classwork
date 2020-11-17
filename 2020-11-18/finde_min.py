array=[int(z) for z in input("Enter numbers: ").split()]
#bable sort
# swap = True
# while swap==True:
#     swap=False
#     for i in range(0,len(array)-1):
#         if array[i]>array[i+1]:
#             swap=True
#             array[i],array[i+1] = array[i+1],array[i]

#finde min

# 1 2 3 4 5 6
# for i in range(0,len(array)):
#     if array[0]>array[i]:
#         array[0],array[i] = array[i],array[0]
min_v = array[0]
for i in range(0,len(array)):
    if min_v>array[i]:
        min_v = array[i]
array[0]=min_v

print(array)