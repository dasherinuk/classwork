# 1 2 3 4 5
# 9 8 1 2 7
# 7 8 1 9 4
# 8 1 4 2 1 
# 0 1 4 2 5

#1 + 8 + 1 + 2+5

user_input=int(input())
main_array=[]
diagonal_array=[]
len_user_input=user_input

for i in range(0,user_input):
    array = [int(r) for r in input().split()]
    main_array.append(array)

for index in range(0,len_user_input):
    array = main_array[index]
    value = array[index]
    diagonal_array.append(value)

print(diagonal_array)


