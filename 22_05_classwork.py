n1=int(input("Enter 1 number"))
n2=int(input("Enter 2 number"))
n3=int(input("Enter 3 number"))

def check(number):
    return number >=94 and number <= 727

if check(n1) and check(n2) and check(n3):
    print(max(n1,n2,n3))
else:
    print("error")
