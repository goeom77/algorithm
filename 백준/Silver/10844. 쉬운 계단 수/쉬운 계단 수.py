# 쉬운 계단 수
# 0 시작 x
N = int(input())
dp = list([0 for i in range(10)] for j in range(N+1))
result = 0
if N > 0:
    dp[1] = [0,1,1,1,1,1,1,1,1,1]
if N > 1:
    dp[2] = [1,1,2,2,2,2,2,2,2,1]
if N > 2:
    for i in range(3,N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1,9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N])%1000000000)