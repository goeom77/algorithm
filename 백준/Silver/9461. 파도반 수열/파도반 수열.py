n = int(input())
a = list(int(input()) for _ in range(n))
b = max(a)
dp = [0]*(b+1)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
if b > 5:
    for k in range(5,b+1,1):
        dp[k] = dp[k-1] + dp[k-5]
for _ in range(n):
    print(dp[a[_]])
