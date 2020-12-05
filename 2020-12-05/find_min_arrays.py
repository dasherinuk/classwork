userInput=input()
aount_list=int(userInput)
main_array=[]
for i in range(0,aount_list):
    array = [int(r) for r in input().split()]
    main_array.append(array)

arra_minimum=[]
for array in main_array:
    arra_minimum.append(min(array))


print(min(arra_minimum))