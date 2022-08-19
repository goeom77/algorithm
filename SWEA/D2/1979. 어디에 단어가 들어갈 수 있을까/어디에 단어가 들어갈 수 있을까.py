T = int(input())
for t in range(1,T+1):
    n,k = map(int,input().split())
    back = [list(map(int,input().split())) for _ in range(n)]
    result_cnt = 0
    for j in range(n):
        cnt = 0

        for i in range(n):
            if back[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result_cnt += 1
                cnt = 0
        if cnt == k:
            result_cnt += 1
    for i in range(n):
        cnt = 0

        for j in range(n):
            if back[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result_cnt += 1
                cnt = 0
        if cnt == k:
            result_cnt += 1
    print(f'#{t} {result_cnt}')


