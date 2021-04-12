a = int(input())
b = int(input())

t = a
a = b
b = t

print(a, b)

a,b = b,a

print(a, b)

array = [a,0,b]

print(array)

array[0],array[2] = array[2],array[0]

print(array)

t = array[0]
array[0] = array[2]
array[2] = t

print(array)
