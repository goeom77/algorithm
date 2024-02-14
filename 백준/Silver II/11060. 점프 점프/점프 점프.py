import sys

input = sys.stdin.readline
# 11060 점프 점프
INF = 1e9
dp = [INF] * 1001
n = int(input())
arr = list(map(int, input().split()))
dp[0] = 1
for i in range(n):
  for j in range(1,arr[i]+1):
    if i+j >= n:
      break
    dp[i+j] = min(dp[i+j], dp[i] + 1)
if dp[n-1] == INF:
  print(-1)
else:
  print(dp[n-1] - 1)