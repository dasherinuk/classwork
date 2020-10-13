def bug_recurcion(s, f):
    if s < f:
        print(s)
        bug_recurcion(s+1,f)


def f(n):
    if n<=1:
        return 1
    return f(n-1)*n

print(f(10))
