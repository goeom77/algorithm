import sys
from collections import deque

a,b,c = map(int,sys.stdin.readline().split())
arr = []
result = []
for i in range(1,a+1):
    arr.append(i)
cnt = 0
cnt_c = 0
q = deque(arr)
while q:
    if cnt_c == 0:
        q.rotate(-b+1)  #시계방향 회전은 양수, 그 반대는 음수
        result.append(q.popleft())
        cnt += 1
        if cnt == c:
            cnt_c -= 1
            cnt = 0
    else:
        q.rotate(b-1)
        result.append(q.pop())
        cnt += 1
        if cnt == c:
            cnt_c += 1
            cnt =0


for i in range(len(result)):
    print(result[i])