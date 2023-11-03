import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 최단 경로 구하기 가중치는 10이하의 자연수
# 정점개수 v, 간선개수 e
# 시작정점 k
V, e = map(int, input().split())
k = int(input())
# 경로 없으면 INF
# u, v , w = u에서 v로 가는 가중치 w
# i번째 줄에 i번째 정점에서 갈 수 있는 정점과 가중치
# 5 - 1 (1)
# 1 - 2 (2)
# 1 - 3 (3)
# 최대값은 600억
INF = int(1e9)
graph = [[] for _ in range(V + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
# 다이스트라 알고리즘
def dijkstra(start):
    distance = [INF] * (V + 1)
    distance[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        # now에서 갈 수 있는 정점들
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance
distance = dijkstra(k)
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])