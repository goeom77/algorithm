import sys
input = sys.stdin.readline
from collections import defaultdict
#n*m 체스판, 안전한 칸의 개수
n, m = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))

safe_zone = n*m
visited = defaultdict(int)

# 장애물 표시 - 1
for i in range(1,queen[0]+1):
    x = queen[2*i-1]
    y = queen[2*i]
    visited[(x,y)] = 1
    # print('queenstate',x,y)
safe_zone -= queen[0]
for i in range(1,(knight[0])+1):
    x = knight[(2*i-1)]
    y = knight[2*i]
    visited[(x,y)] = 1
    # print('knightstat',x,y)
safe_zone -= knight[0]
for i in range(1,(pawn[0])+1):
    x = pawn[(2*i-1)]
    y = pawn[2*i]
    visited[(x,y)] = 1
    # print('pawnstate',nx,ny)
safe_zone -= pawn[0]
for i in range(1,queen[0]+1):
    for dx, dy in [(1,0),(-1,-1),(-1,0),(-1,1),(0,1),(1,-1),(0,-1),(1,1)]:
        # 위치 초기화
        x = queen[(2*i-1)]
        y = queen[2*i]
        while True:
            x += dx
            y += dy
            # 범위 밖
            if x < 1 or y <1 or x > n or y > m:
                break
            # 장애물 존재
            if visited[(x,y)] == 1:
                break
            # 누가 들린곳
            elif visited[(x,y)] == 2:
                continue
            visited[(x,y)] = 2
            safe_zone -= 1
            # print('queenmove',x,y)
for i in range(1,(knight[0])+1):
    x = knight[(2*i-1)]
    y = knight[2*i]
    # print('knightstat',x,y)
    for dx,dy in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
        nx = x + dx
        ny = y + dy
        # 범위 내라면
        if 1 <= nx <= n and 1 <= ny <= m and not visited[(nx,ny)]:
            # 아무도 안들렸다면
            visited[(nx,ny)] = 2
            safe_zone -= 1
            # print('nightmove',nx,ny)
print(safe_zone)