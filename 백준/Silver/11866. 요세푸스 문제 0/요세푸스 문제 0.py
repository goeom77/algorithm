import sys
from collections import deque

a,b = map(int,sys.stdin.readline().split())
arr = []
result = []
for i in range(1,a+1):
    arr.append(i)

q = deque(arr)
while q:
    q.rotate(-b+1)  #시계방향 회전은 양수, 그 반대는 음수
    result.append(q.popleft())

print('<',end="")
print(*result,sep=", ",end="")
print(">")