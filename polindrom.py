line = input()
polindrom = "YES"
for i in range(len(line)//2):
    if line[i]!=line[len(line)-1-i]:
        polindrom = "NO"

print(polindrom)
        
