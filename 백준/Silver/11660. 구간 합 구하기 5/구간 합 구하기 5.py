from sys import stdin

n,m = map(int, stdin.readline().split())
lista=[[0]*(n+1)]
for i in range(n):
    lista.append([0]+list(map(int, stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, n):
        lista[i][j+1] += lista[i][j]

for j in range(1, n+1):
    for i in range(1, n):
        lista[i+1][j] += lista[i][j]


res=[]
for i in range(m):
    cord=list(map(int, stdin.readline().split()))
    corda=cord[:2]
    cordb=cord[2:]
    res.append(lista[cordb[0]][cordb[1]]-lista[cordb[0]][corda[1]-1]-lista[corda[0]-1][cordb[1]]+lista[corda[0]-1][corda[1]-1])

for ele in res:
    print(ele)