# 포도주
# 다 마시고 그자리에 두기
# 연속 3개 금지
N = int(input())
soju = [0]*(N+1)
for i in range(N):
    soju[i+1] = int(input())
dp= [0]*(N+1)
result = 0
if N > 0:
    dp[1] = soju[1]
    result = dp[1]
if N > 1:
    dp[2] = dp[1] + soju[2]
    result = dp[2]
if N > 2:
    for i in range(3,N+1):
    # dp[3] = dp[1] + soju[3], dp[0] + soju[2] + soju[3]
        dp[i] = max(dp[i-2] + soju[i],dp[i-3]+soju[i-1]+soju[i],dp[i-1])
        if dp[i] > result:
            result = dp[i]
print(result)