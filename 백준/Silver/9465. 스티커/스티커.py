# 스티커
# 상하좌우 못쓰게 된다.
T = int(input())
for t in range(T):
    n = int(input())
    sticker = [list(map(int,input().split())) for _ in range(2)]
    dp = [0,0,0] # 위를 더한 경우, 밑을 더한경우, 안 더한 경우
    result = [0,0,0]
    for i in range(n):
        dp = result[:]
        result[0] = sticker[0][i] + max(dp[1],dp[2])
        result[1] = sticker[1][i] + max(dp[0],dp[2])
        result[2] = max(dp[0],dp[1],dp[2])
    print(max(result))