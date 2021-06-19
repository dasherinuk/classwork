days=int(input("Enter amount of days"))
flowers = ["G","C","V"]
for i in range(0,days):
    flowers[1],flowers[-1] = flowers[-1],flowers[1]
    flowers[0],flowers[1] = flowers[1],flowers[0]
    

print(flowers)
#if days==
#g k f
#g f k
#f g k
#f k g
#k f g
#k g f
#g k f
