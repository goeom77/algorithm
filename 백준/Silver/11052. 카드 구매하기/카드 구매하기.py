import sys

input = sys.stdin.readline
# 11052 카드 구매하기
N = int(input())
P = [0] + list(map(int, input().split()))
# N개의 카드를 구매하는 최대 비용
# P는 p[n]에서 n개의 카드를 사는 비용
dp = [0] * (N + 1)
dp[1] = P[1]
for i in range(2, N+1):
  for j in range(1, i+1):
    dp[i] = max(dp[i], dp[i-j] + P[j])
print(dp[N])