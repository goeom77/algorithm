# n과 m(5)
# 길이가 m인 수열 모두 구하기

def combo(n,m):
    if n==m:
        print(*chosen)
        return
    for i in range(len(arr)):
        if arr[i] in chosen:
            continue
        chosen[n] = arr[i]
        combo(n+1,m)
        chosen[n] = 0

n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
chosen = [0]*m
combo(0,m)
