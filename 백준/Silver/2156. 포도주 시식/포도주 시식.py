import sys
from itertools import combinations

input = sys.stdin.readline
# 2156 포도주 시식
n = int(input())
wine = [int(input()) for _ in range(n)]
# n개의 포도주가 주어졌을 때, 최대로 마실 수 있는 포도주의 양을 구하라, 3번 연속으로 마실 수 없다.
dp = [0] * n
dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]
    if n > 2:
        dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])
        for i in range(3, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])
print(dp[-1])