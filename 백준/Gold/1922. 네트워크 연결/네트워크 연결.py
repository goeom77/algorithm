# 1922 네트워크 연결
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
M = int(input())

# 모든 컴퓨터를 연결하는 최소 비용
heap = []
for _ in range(M):
  a, b, cost = map(int, input().split())
  heappush(heap, (cost, a, b))

parent = [i for i in range(N+1)]

def findParent(x):
  if parent[x] == x:
    return x
  parent[x] = findParent(parent[x])
  return parent[x]
  
def union(a, b):
  a = findParent(a)
  b = findParent(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

result = 0
while heap:
  cost, a, b = heappop(heap)
  if findParent(a) != findParent(b):
    union(a, b)
    result += cost

print(result)