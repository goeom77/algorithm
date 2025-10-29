def solution(n, computers):
    answer = 0
    # 연결이 되어있는가, 아닌가로 분리
    visited = [False] * (n)
    q = []
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        answer += 1
        q.append(i)
        while q:
            node = q.pop()
            for i in range(n):
                tmp = computers[node][i]
                print('tmp : ' + str(tmp))
                if tmp and not visited[i]:
                    visited[i] = True
                    q.append(i)
        
        
    return answer