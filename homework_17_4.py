#1 2 9 4 7 5 1 4 0 10 3 9
#1 9
#1 9
#0 10
#7 3


array=[]
amount_elements=int(input("Enter amount of elements"))
first_num=int(input("Enter the first number"))
second_num=int(input("Enter the second number"))

for i in range(first_num,second_num):
    num=first_num+i
    array.append(num)

##for i in range(0,amount_elements):
##    elements=int(input("Enter an element"))
##    array.append(elements)

for i in range(0,amount_elements):
    for j in range(i+1,amount_elements):
        for k in range(j+1,amount_elements):
            for l in range(k+1,amount_elements):
                s = array[i]+array[j]+array[k]+array[l]
                if s>=first_num and s<=second_num:
                    print(i,j,k,l,m)


print("=================")
for i in range(0,amount_elements):
    print(i, array[i])

