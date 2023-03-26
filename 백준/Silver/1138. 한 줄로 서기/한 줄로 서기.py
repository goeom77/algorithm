import sys
input = sys.stdin.readline

# n명이 한줄 서기
# 자기보다 큰사람이 왼쪽에 몇명인지만 기억한다. 
# 사람 수 n 키는 1~n 까지
N = int(input())
LW = list(map(int, input().split()))
# 1인 사람의 왼쪽에 몇명있는지
result = [N]*N
for i in range(N):
    h = i + 1
    order = LW[i]
    cnt = 0
    for j in range(N):
        if cnt == order:
            if result[j] != N:
                continue
            else:
                result[j] = h
                break
        if result[j] > h:
            cnt += 1
            
print(*result)