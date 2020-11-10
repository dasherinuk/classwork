#hello world
#3 1 2 4
#hell|o wo|rld
#lhel|wo o|rld

open_text = list(input("enter open text: "))#str to list char
key = [int(z)-1 for z in input("Enter key: ").split()]

if len(key)!=4:#todo
    print("error key")
else:
    list_char=[]
    for i in range(0, len(open_text)-3,4):#todo
        #i, i+1, i+2, i+3
        #todo for range(len(key))
        list_char.append(open_text[i+0])
        list_char.append(open_text[i+1])
        list_char.append(open_text[i+2])
        list_char.append(open_text[i+3])
        #todo for range(len(key))
        open_text[i+0] = list_char[key[0]]
        open_text[i+1] = list_char[key[1]]
        open_text[i+2] = list_char[key[2]]
        open_text[i+3] = list_char[key[3]]

    print(*open_text,sep="")