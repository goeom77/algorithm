from collections import deque
def solution(maps):
    row = len(maps[0])
    col = len(maps)
    MXVALUE = row*col + 1
    answer = MXVALUE
    q = deque([(1,0,0)])
    visited = [[False] * row for _ in range(col)]
    while q:
        (d,x,y) = q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= row or ny <0 or ny >= col:
                continue
            if visited[ny][nx] or maps[ny][nx] == 0:
                continue
            if (nx,ny) == (row-1,col-1):
                answer = min(d+1,answer)
            visited[ny][nx] = True
            q.append((d+1,nx,ny))
            
    if answer == MXVALUE:
        answer = -1
    return answer