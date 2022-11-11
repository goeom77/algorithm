# 계단
# 한계단, 두계단 오를수 있다
# 마지막 계단은 무조건 밟아야 한다.
# 세계단 연속 밟을수 없다.
# 한계단 다음은 두계단 밟아야하네 연속 두계단은 가능하고
N = int(input())
stair = [0]*(N+1)
for i in range(1,N+1):
    stair[i] = int(input())
# print(stair)
dp = [0]*(N+1)
# print(dp)
if N > 0:
    dp[1] = stair[1] # 1번째 계단
if N > 1:
    dp[2] = dp[1] + stair[2] # 2번째 계단
if N > 2:
    # dp[3] = max(dp[1] + stair[3],dp[0] + stair[2]+stair[3]) # 3개 연속 밟을 수 없으니깐
# dp[4] = max(dp[2]+stair[4],dp[1]+stair[3]) # 최대 2에서 오는것, 최대 1 + 2칸 + 1칸인 경우
# if N > 3:
    for i in range(3,N+1):
        dp[i] = max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])
print(dp[N])