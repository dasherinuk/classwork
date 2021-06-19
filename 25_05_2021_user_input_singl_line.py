##a = input() #1
##print(a)
##list_input = a.split() #2
##print(list_input)
##for i in range(len(list_input)): #3
##    list_input[i] = int(list_input[i]) #4
##print(list_input)

# 2 values
a,b = [int(item) for item in input().split()] # 1 2 3 4 
print(a + b)

#3 values
a,b,c = [int(item) for item in input().split()] # 1 2 3 4 
print(a + b + c)

#4 values
a,b,c,d = [int(item) for item in input().split()] # 1 2 3 4 
print(a + b + c + d)

#list 
lst = [int(item) for item in input().split()] # 1 2 3 4 
print(sum(lst))
