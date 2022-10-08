n, d = map(int, input().split())
# 최대가 10000개이기 때문에 다 익스트라로 하기에는 조금 많음
# 지름길 개수, 총거리
INF = int(1e8)
short_cut = []
dp = [INF]*(d+1)
for i in range(n):
    a, b, c = map(int, input().split())
    # 출발 도착 길이
    if b-a < c:
        continue
    else:
        short_cut.append((a,b,c))
        # 지름길 a 에서 b로 가는데 c가 걸린다.
short_cut.sort(key=lambda x:(x[1],x[0]))

dp[0] = 0
cnt = 0
for j in range(d+1):
    if j >0:
        dp[j] = dp[j-1]+1
        # 한칸씩 커진다.
    while cnt < len(short_cut) and short_cut[cnt][1] == j:
        dp[short_cut[cnt][1]] = min(dp[short_cut[cnt][0]] + short_cut[cnt][2], dp[short_cut[cnt][1]])
            # 거리를 더한 것 보다 작으면 이 지름길을 이용한다.
            # 이 조건을 이용하기 위해서는 위에 방법처럼 sort할 필요가 있다.
            # 짧은 길부터 비교해야 모든 길을 비교 할 수 있기 때문이다.
        cnt += 1

print(dp[d])
