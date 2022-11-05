import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
result = arr[0]
dp = arr[0]
for i in range(1,n):
    if arr[i] > dp+arr[i]:
        dp = arr[i]
    elif dp+arr[i] >0:
        dp += arr[i]
    else:
        dp = arr[i]
    if dp > result:
        result = dp
print(result)