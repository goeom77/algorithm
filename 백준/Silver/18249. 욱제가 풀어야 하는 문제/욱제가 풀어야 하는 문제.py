# n 1~191229
# n개 정점 빨강, 파랑
import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 191230
MOD = int(1e9 + 7)
dp[1] = 1
dp[2] = 2
for i in range(3,191230):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD
for t in range(T):
    n = int(input())
    # 일자로 잇거나, x자로 잇는 것 2개만 있을 듯
    # 모든 경우의 수는?
    print(dp[n])