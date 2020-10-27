array=[]
n = int(input("Enter amount numbers: "))
for i in range (0,n):
    Userinput=int(input("Enter a number: "))
    array.append(Userinput)

correct=True
for i in range(n//2):
    #0 -1-0 = -1
    #1 -1-1 = -2
    #2 -1-2 = -3
    #3 -1-3 = -4
    if array[i]!=array[-1-i]:
        correct=False
        break
print(correct)
