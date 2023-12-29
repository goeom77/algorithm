import sys
from collections import deque
input = sys.stdin.readline
# 1261 알고 스팟
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(m)]
# 0,0 -> n-1, m-1까지 가는데 뚫어야할 벽의 최소 개수
visited = [[-1]*n for _ in range(m)]
visited[0][0] = 0
q = deque([(0,0)])
# 전형적인 0-1 bfs문제이다. 오래걸리는 것은 뒤로넣고 빠른 것은 앞으로 넣어서 처리하기
while q:
  if visited[m-1][n-1] != -1:
    break
  x, y = q.popleft()
  for dx, dy in [(0,-1),(-1,0),(1,0),(0,1)]:
    nx = x + dx
    ny = y + dy
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if arr[ny][nx] == "1" and (visited[ny][nx] == -1 or visited[ny][nx] > visited[y][x] + 1):
      visited[ny][nx] = visited[y][x] + 1
      q.append((nx,ny))
    elif arr[ny][nx] == "0" and (visited[ny][nx] == -1 or visited[ny][nx] > visited[y][x]):
      visited[ny][nx] = visited[y][x]
      q.appendleft((nx,ny))
print(visited[m-1][n-1])