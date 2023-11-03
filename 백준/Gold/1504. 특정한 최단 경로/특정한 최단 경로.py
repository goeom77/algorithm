import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = int(1e9)
n, e = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
v1, v2 = map(int, input().split())
# v1, v2를 무조건 거쳐야 한다.
def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    q = []
    heappush(q,(0,start))
    while q:
        d, now = heappop(q)
        if dist[now] < d:
            continue
        for i in arr[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heappush(q,(cost,i[0]))
    return dist
dist0 = dijkstra(1)
distv1 = dijkstra(v1)
distv2 = dijkstra(v2)
# 0 -> v1 -> v2 -> n
dist0V1V2 = dist0[v1] + distv1[v2] + distv2[n]
# 0 -> v2 -> v1 -> n
dist0V2V1 = dist0[v2] + distv2[v1] + distv1[n]
result = min(dist0V1V2, dist0V2V1)
if result >= INF:
    print(-1)
else:
    print(result)