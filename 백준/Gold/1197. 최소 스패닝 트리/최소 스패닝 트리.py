# 최소 스패닝 트리

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent,parent[x])
    return parent[x]
# root는 부모가 없으니깐 그것을 찾을 때

def union(parent, a,b):
    rootA = find(parent,a)
    rootB = find(parent,b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

V, E = map(int, input().split())
parent = [0]*(V+1)

edges = []
answer = 0

for i in range(1,V+1):
    parent[i] = i
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a,b)
        answer += cost
print(answer)