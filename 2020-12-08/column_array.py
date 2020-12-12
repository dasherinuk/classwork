

user_input=int(input())
main_array=[]
new_array=[]


for i in range(0,user_input):
    array = [int(r) for r in input().split()]
    main_array.append(array)



for row in range(0,user_input):
    array = main_array[row]
    array[row],array[-row-1]=array[-row-1],array[row]
    new_array.append(array)


print(*new_array, sep="\n")


