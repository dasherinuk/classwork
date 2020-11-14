enter_text=list(input("Enter your text: "))# abcdef
key=[int(p)-1 for p in input("Enter key: ").split()] #3 2 1
# a b c d e f    enter_text
# 0 1 2 3 4 5    enter_text index

# 2 1 0          key

len_key=len(key)# 3

if len_key>len(enter_text):
    print("Incorrect key")
else:
    # for i in range(0, 8, 5) # 0 5
    # for i in range(0, 7, 9) # 0
    # for i in range(0, 19, 6) # 0 6 12 18
    # for i in range(0, 18, 6) # 0 6 12
    # for i in range(0, 10, 2) # 0 2 4 6 8
    # for i in range(3, 5, 2) # 3
    # for i in range(0, -10, -3)  #  0 -3 -6 -9
    # for i in range(10, -1, 8) # none
    #
    #for i in range(0,4,3):
    for i in range(0,len(enter_text)-(len_key-1),len_key):# 0 3 
        array=[]#contain copy change part of  enter_text
        for b in range(len_key):# 0 1 2
            array.append(enter_text[i+b])# i = 0    i+b 0 1 2 
                                         # i = 3    i+b 3 4 5
        for b in range(len_key):# 0 1 2 
            enter_text[i+b] = array[key[b]]

    print(*enter_text, sep="")



