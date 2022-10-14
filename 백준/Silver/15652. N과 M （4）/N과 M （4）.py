# n m
def perm(n,m,j):
    if n== m:
        print(*chosen)
        return
    for i in range(j,len(arr)):
        chosen[n] = arr[i]
        perm(n+1,m,i)

N,M = map(int, input().split())
arr = list(range(1,N+1))
chosen = [0]*M
perm(0,M,0)