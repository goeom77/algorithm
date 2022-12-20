# 2등 찾기
import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())

    # 종료 조건
    if (n,m) == (0,0):
        break

    # n주간 정보, m명
    ranking = [[0,i] for i in range(10001)]
        # 점수 선수 번호

    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(len(arr)):
            ranking[arr[j]][0] += 1

    ranking.sort(key=lambda x: [-x[0],x[1]])
    second = ranking[1][0]
    flag = True
    result = []
    for i in range(1,10001):
        if ranking[i][0] == second:
            result.append(ranking[i][1])
        else:
            break
    print(*result)
    
