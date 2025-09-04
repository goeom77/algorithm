def solution(storage, requests):
    r = len(storage[0])
    c = len(storage)
    # storage만 r,c의 길이가 작게 설정(주변 테두리를 둘렀기 떄문)
    goods = [[False]*(r+2)] + [([False] + [True]*r + [False]) for _ in range(c)] + [[False]*(r+2)]
    for i in range(len(requests)):
        # i : 몇번째 요청인가
        n = len(requests[i])
        # 확인했던 곳들

        if (n == 1):
            visited = [[False]*(r+2) for _ in range(c+2)]
            visited[0][0] = True
            q = [(0,0)]
            # 외곽에서 접근 가능한 곳에서 확인
            while(q):
                x, y = q.pop()
                for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nx = x + dx
                    ny  = y + dy
                    if (nx <0 or nx >= r+2 or ny < 0 or ny >= c+2):
                        continue
                    if visited[ny][nx]:
                        continue
                    # 물건이 없으면
                    if not goods[ny][nx]:
                        q.append((nx,ny))
                        visited[ny][nx] = True
                        continue
                    # 물건이 있는데 똑같으면
                    if storage[ny-1][nx-1] == requests[i]:
                        # visited처리해서 다시 오지 않도록 설정
                        visited[ny][nx] = True
                        goods[ny][nx] = False
        if (n == 2):
            value = requests[i][0]
            for cc in range(1,c+1,1):
                for rr in range(1,r+1,1):
                    if goods[cc][rr] and storage[cc-1][rr-1] == value:
                        goods[cc][rr] = False
    
    answer = 0
    for cc in range(c+2):
        for rr in range(r+2):
            if goods[cc][rr]:
                answer+=1

    return answer