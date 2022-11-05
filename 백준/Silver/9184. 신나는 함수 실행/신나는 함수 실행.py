import sys
input = sys.stdin.readline
dp=list(list([0]*21 for i in range(21)) for j in range(21))
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j== 0 or k== 0:
                dp[k][j][i] = 1
for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i < j and j < k:
                dp[k][j][i] = dp[k-1][j][i] + dp[k-1][j-1][i] - dp[k][j-1][i]
            else:
                dp[k][j][i] = dp[k][j][i-1] + dp[k][j-1][i-1] + dp[k-1][j][i-1] - dp[k-1][j-1][i-1]

while True:
    a , b, c = map(int, input().split())
    if (a,b,c) == (-1,-1,-1):
        break
    if a<=0 or b <=0 or c <= 0:
        result = 1
    elif a>20 or b>20 or c>20:
        result = dp[20][20][20]
    else:
        result = dp[c][b][a]

    print(f'w({a}, {b}, {c}) = {result}')
