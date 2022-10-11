# n*n 어항에서 m마리 물고기와 1마리 상어
# 처음 아기 상어 크기는 2
# 상하좌우 이동
# 자기보다 큰 물고기가 있는 칸은 지나 갈수 없다.
# 자기보다 작은 물고기만 먹을수 있고 같은 물고기는 지나갈수있다.
# 먹을 수 있는 물고기가 1마리보다 많으면 칸의 최솟값을 가지는 먹이 먹기
# 같다면 가장 위, 왼쪽에 있는 물고기를 먹는다.
# 자기 크기와 같은 수의 물고기 먹으면 크기 1 증가
# 걸리는 시간 출력
from collections import deque
n = int(input()) # n 2~20
fishbowl = [list(map(int, input().split())) for _ in range(n)]
# 0 빈칸, 123456 물고기 크기 , 9 아기상어
size = 2
eat = 0
time = 0

def where_shark(): # 처음 상어의 위치 찾기
    for j in range(n):
        for i in range(n):
            if fishbowl[j][i] == 9:
                fishbowl[j][i] = 0
                return (j,i)

def where_eat(y,x,size):
    global eat
    global eat_width
    global n
    # 아기 상어 위치와 size를 받아서 갈수 있는 곳중 가장 가까운곳 BFS로 찾기
    visited = [[-1]*n for _ in range(n)]
    what_eat = [] # 먹을 것을 넣어두고 그 중에서 가장 가깝고 상좌를 선택
    q = deque([(y,x)])
    visited[y][x] = 0
    while q:
        j,i = q.popleft()
        if visited[j][i] > eat_width: # BFS 범위를 넘어서게 된다면
            what_eat.sort()
            rj, ri = what_eat[0]
            fishbowl[rj][ri] = 0
            eat += 1
            return (rj,ri,eat_width)

        for di,dj in [[0,-1],[-1,0],[1,0],[0,1]]:
            ni = i + di
            nj = j + dj
            if ni<0 or nj<0 or ni>=n or nj>=n or visited[nj][ni] != -1 or fishbowl[nj][ni]>size:
                continue
            q.append((nj,ni)) # 이동 가능 리스트에 넣기
            visited[nj][ni] = visited[j][i] + 1 # 이동한 거리를 기록
            if 0 < fishbowl[nj][ni] < size: # 먹을 수 있는 먹이가 있다면
                if eat_width >= visited[nj][ni]:
                    eat_width = visited[nj][ni] # BFS의 범위를 고정
                    what_eat.append((nj,ni)) # 먹을 것들 넣기
                # fishbowl[nj][ni] = 0
                # eat += 1
                # return (nj,ni,visited[nj][ni])
    if what_eat:
        what_eat.sort()
        rj, ri = what_eat[0]
        fishbowl[rj][ri] = 0
        eat += 1
        return (rj,ri,eat_width)
    return (0,-1,0) # 먹을 것이 없으면

j,i = where_shark()
while True:
    eat_width = 500
    nj,ni,d = where_eat(j,i,size)
    if ni == -1: # 먹을게 없으면
        break
    if eat == size: # 먹은 량이랑 상어크기가 같으면
        size += 1 # 상어의 크기를 키워준다.
        eat = 0
    time += d # 이동한 거리만큼 더해준다.
    i,j = ni,nj # 상어의 위치 변경
print(time)
