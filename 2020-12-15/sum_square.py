# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 + 1 + 1 + 1 + 2 + 3  + 4 + 2 + 3 + 4 + 4 + 4
#add first row
#add last row
#add eveything in first column except last and first
#add all

input_user=int(input())
main_array=[]




for i in range(0,input_user):
    array = [int(r) for r in input().split()]
    main_array.append(array)
len_array=input_user


add_first=sum(main_array[0])
add_last=sum(main_array[-1])

add_firs_col=0
for ind in range(1,len_array-1):
    add_firs_col+=main_array[ind][0]
add_last_col=0
for index in range(1,len_array-1):
    add_last_col+=main_array[index][len_array-1]

print(add_first+add_last+add_firs_col+add_last_col)
    
    



