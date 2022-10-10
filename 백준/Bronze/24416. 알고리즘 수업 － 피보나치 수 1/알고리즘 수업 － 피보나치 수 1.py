f = [1, 1]
for i in range(2, int(input())):
    f += [f[i-1]+f[i-2]]
print(f[-1],len(f)-2)