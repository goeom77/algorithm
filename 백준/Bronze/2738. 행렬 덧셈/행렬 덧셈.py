n,m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
brr = [list(map(int, input().split())) for _ in range(n)]
for j in range(n):
    for i in range(m):
        print(arr[j][i] + brr[j][i],end=" ")
    print()
