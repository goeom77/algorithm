# A = S극으로 향함
# B = N극으로 향함
# D = 파랑이 한개라도 있으면 교착
# 교착상태의 개수를 세어라
# 1 -> N 밑으로 떨어짐 2 -> S 위로 올라감
for t in range(1,11):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(matrix[j][i])
        if 1 in arr and 2 in arr:
            cnt = 0
            stack = 0
            for k in range(n):
                if arr[k] == 2:
                    if stack == 1:
                        cnt += 1
                    stack = 2
                elif arr[k] == 1:
                    stack = 1
            result += cnt
    print(f'#{t} {result}')