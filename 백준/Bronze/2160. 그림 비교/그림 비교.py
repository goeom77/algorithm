# 그림 비교
import sys
input = sys.stdin.readline

# 브루트 포스말고는 생각 나지 않는다.
# n은 arr.length
n = int(input())
# 최대 50개 *5*7니깐 많은 메모리를 잡진 않는 것같다.
arr = []
for i in range(n):
    tmp = [list(input()) for _ in range(5)]
    arr.append(tmp)

result = 35
answer = [1,2]
for j in range(n-1):
    for i in range(j+1,n):
        # idx - 1 이 비교된다.
        cnt = 0
        for dj in range(5):
            for di in range(7):
                if arr[j][dj][di] != arr[i][dj][di]:
                    cnt += 1
        if result > cnt:
            answer[0] = j + 1
            answer[1] = i + 1
            result = cnt
print(answer[0],answer[1])