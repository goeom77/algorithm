import sys
input = sys.stdin.readline
# 16948 데스 나이트
move = [(-2,-1),(2,-1),(-2,1),(2,1),(0,-2),(0,2)]
n = int(input())
r1,c1,r2,c2 = map(int,input().split())
visited = [[0]*n for _ in range(n)]
def bfs():
    q = [(r1,c1)]
    visited[r1][c1] = 1
    while q:
        x,y = q.pop(0)
        if x == r2 and y == c2:
            return visited[x][y]-1
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
    return -1
print(bfs())