import heapq
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
s = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
# x 에서 출발한다고 생각하자
for i in range(m):
    a,b,c = map(int,input().split())
    # a -> b 가는데 c 소모
    graph[a].append((b,c))

distance = [INF]*(n+1)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(s)
for i in range(1,n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
