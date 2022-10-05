# n과 m(8)
# 길이가 m인 수열 모두 구하기

def combo(n,m,j):
    if n==m:
        print(*chosen)
        return
    for i in range(j,len(arr)):
        chosen[n] = arr[i]
        combo(n+1,m,i)

n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
chosen = [0]*m
combo(0,m,0)
