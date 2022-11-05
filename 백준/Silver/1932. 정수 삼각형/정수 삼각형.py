n = int(input())
arr = []
for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)
result = []
for i in range(1,n):
    a = [0]*i
    result.append(a)
result.append(arr[-1])
while n != 0:
    n -= 1
    for k in range(n):
        if result[n][k] > result[n][k+1]:
            tmp = result[n][k]
        else:
            tmp = result[n][k+1]
        result[n-1][k] = arr[n-1][k] + tmp
print(result[0][0])