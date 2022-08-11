N,T = map(int,input().split())
pocket1 = {'0':'aa'}
pocket2 = {'aa':'0'}
for n in range(1,N+1):
    a = input()
    pocket1[str(n)] = a
    pocket2[a] = n

for t in range(T):
    b = input()
    if b.isdecimal():
        c = pocket1[b]
        print(c)
    else:
        d =pocket2[b]
        print(d)