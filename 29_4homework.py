multiply=2
sum1 = 1
for i in range(0,50):
    if i%3==0:
        sum1=sum1*multiply
        multiply*=2
        print(sum1, end=" ")
    elif i%3==1:
        print(0, end=" ")
    else:
        sum1 = sum1//2
        print(sum1, end=" ")
    
