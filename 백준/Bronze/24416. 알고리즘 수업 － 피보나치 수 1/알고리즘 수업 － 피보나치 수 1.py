n = int(input())

f = [1, 1]
for i in range(2, n):
    f += [(f[i-1]+f[i-2])]

print(f[n-1], n-2)