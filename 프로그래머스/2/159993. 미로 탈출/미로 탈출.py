from collections import deque
def solution(maps):
    # s -> l -> e
    n = len(maps[0])  # 가로
    m = len(maps)  # 세로
    StoL = [[-1]*n for _ in range(m)]
    LtoE = [[-1]*n for _ in range(m)]
    E = None
    for row in range(m):
        for col in range(n):
            if maps[row][col] == "S":
                S = (row, col)
                StoL[row][col] = 0
                break

    SLq = deque([S])
    LEq = deque()

    def SLbfs():
        while(SLq):
            row, col = SLq.popleft()
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr = dr + row
                nc = dc + col
                if nr >= m or nr < 0 or nc >= n or nc < 0:
                    continue
                if maps[nr][nc] == "L":
                    LEq.append((nr, nc))
                    LtoE[nr][nc] = 0
                    return StoL[row][col] + 1
                if maps[nr][nc] != "X" and StoL[nr][nc] == -1:
                    SLq.append((nr, nc))
                    StoL[nr][nc] = StoL[row][col] + 1
        return -1

    def LEbfs():
        while(LEq):
            row, col = LEq.popleft()
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr = dr + row
                nc = dc + col
                if nr >= m or nr < 0 or nc >= n or nc < 0:
                    continue
                if maps[nr][nc] == "E":
                    return LtoE[row][col] + 1
                if maps[nr][nc] != "X" and LtoE[nr][nc] == -1:
                    LEq.append((nr, nc))
                    LtoE[nr][nc] = LtoE[row][col] + 1
        return -1

    sl = SLbfs()

    if sl == -1:
        return -1
    le = LEbfs()
    if le == -1:
        return -1

    return sl + le