sum1=100
for i in range(25):
    print(sum1)
    if i% 4==0:
        sum1//=2
    elif i % 4==1:
        sum1+=2
    elif i %4==2:
        sum1-=1
    else:
        sum1*=2
