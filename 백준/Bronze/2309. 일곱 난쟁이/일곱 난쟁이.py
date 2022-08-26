k = []
for i in range(9):
    k.append(int(input()))

for i in k:
    for j in k:
        if sum(k) - i - j == 100 and i != j:
            k.remove(i)
            k.remove(j)

k.sort()
print(*k,sep="\n")