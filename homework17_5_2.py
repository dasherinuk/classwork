n=int(input("Enter number"))

sum1=0
for i in range(0,n):
    sum1+=i


sum2=0
for i in range(1,n+1):
    sum2+=i


sum3=0
for i in range(0,n):
    sum3+=i+1

print(sum1, sum2, sum3)
