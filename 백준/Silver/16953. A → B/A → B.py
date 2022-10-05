# A->B
from collections import deque,defaultdict
# 1. 2곱하기 , 1을 수의 가장 오른쪽에 추가
a,b = map(int,input().split())
dp = defaultdict(int)
dp[a] = 1
q = deque([a])
while q and dp[b]==0:
    st = q.popleft()
    c = st*2
    d = st*10+1
    if c <= b:
        dp[c] = dp[st]+1
        q.append(c)
    if d <= b:
        dp[d] = dp[st]+1
        q.append(d)
if dp[b]:
    print(dp[b])
else:
    print('-1')
