import sys

input = sys.stdin.readline
# 1303 전쟁 - 전투
# 아군 W, 적군 B
# dfs로 풀어서 최댓값
n, m = map(int, input().split()) # n: 가로, m: 세로
w, b = 0, 0
visited = [[False] * n for _ in range(m)]
board = [list(input().rstrip()) for _ in range(m)]
def dfs(i, j): 
  global cnt
  visited[j][i] = True
  cnt +=  1
  for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    ni, nj = i + di, j + dj
    if 0 <= ni < n and 0 <= nj < m and not visited[nj][ni] and board[nj][ni] == board[j][i]:
      dfs(ni, nj)
  return cnt
for i in range(n):
  for j in range(m):
    if not visited[j][i]:
      cnt = 0
      dfs(i, j)
      if board[j][i] == 'W':
        w += cnt **2
      else:
        b += cnt **2
print(w,b)