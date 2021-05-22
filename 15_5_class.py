# две коровы
# количесво денй
#сначал вводим данные за пять дней для первой коровы
#потом за пять дней ля второй
#5 6 3 1 9
#2 6 1 9 9

cow1=[]
cow2=[]
days=int(input("How many days?"))
for i in range(days):
         litres1=int(input("Enter the amount of litres"))
         cow1.append(litres1)
         
for i in range(days):
         litres2=int(input("Enter the amount of litres"))
         cow2.append(litres2)

sum1=0
for i in range(days):
         sum1+=cow1[i]
sum2=0
for i in range(days):
    sum2+=cow2[i]

if sum1>sum2:
    print(sum1," cow 1 gave more milk")
else:
    print(sum2,"cow2 gave more milk")
         
        
