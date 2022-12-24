def rev(n):
    n = list(str(n))
    n.reverse()
    n = int(''.join(n))
    return n

a, b = map(int, input().split(" "))
a = rev(a)
b = rev(b)
print(rev(a+b))