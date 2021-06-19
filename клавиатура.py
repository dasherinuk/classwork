array=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","k","l","z","x","c","v","b","n","m"]
userinput=input("Enter a letter")

##if userinput=='m':
##    print("q")
##else:
##    for i in range(len(array)):
##        if userinput==array[i]:
##            print(array[i+1])

print(array[(array.index(userinput)+1)%len(array)])
