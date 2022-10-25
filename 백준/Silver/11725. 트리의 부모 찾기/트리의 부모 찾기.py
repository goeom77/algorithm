# root = 1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
visited = [0]*(n+1)
graph = {}
for tmp in range(1,n+1):
    graph[tmp] = []
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1] = 1
def search(n):
    global visited
    for i in graph[n]:
        if visited[i] == 0:
            visited[i] = n
            search(i)
        
search(1)
for j in range(2,n+1):
    print(visited[j])