n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))


arr_pairs = []

for i in range(0, n-n%2, 2):
    arr_pairs.append([arr[i],arr[i+1]])

if n%2==1:
    arr_pairs.append([arr[-1],0])

print(arr_pairs)
