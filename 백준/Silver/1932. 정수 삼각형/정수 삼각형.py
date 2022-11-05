import sys
input = sys.stdin.readline
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
        result[n-1][k] = arr[n-1][k] + max(result[n][k],result[n][k+1])
print(result[0][0])