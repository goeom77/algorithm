# 피보나치 수1
n = int(input())
dp = [0]*(n+1)
dp[1] = 1
dp[2] = 1
for j in range(3,n+1):
    dp[j] = dp[j-1] + dp[j-2]

print(dp[n],n-2)
