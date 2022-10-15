# 파티
# n개 마을에 한명씩 n명 학생이 x 마을에서 파티
# m개의 단방향 도로, i번째 길을 지나는데 Ti소모
# 최단 시간 소모할 때 가장 오래 걸리는 학생 누구인지
import heapq
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e7)
# x 에서 출발한다고 생각하자
for i in range(m):
    a,b,c = map(int,input().split())
    # a -> b 가는데 c 소모
    graph[a].append((b,c))


def dijkstra(start,end):
    distance = [INF]*(n+1)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]

result = 0 # 초기값 설정
for i in range(1,n+1):
    go = dijkstra(i,x) # 갈때 최소값
    back = dijkstra(x,i) # 올때 최소값
    result = max(result,go+back)

print(result)