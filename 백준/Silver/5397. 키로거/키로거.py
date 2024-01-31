import sys
from collections import deque
input = sys.stdin.readline
#5397 키로거
# 알파벳 대소문자, 숫자, 백스페이스(-), 화살표 사용가능(<,>)
# - 하나 지우기
# < 왼쪽으로 한칸
# > 오른쪽으로 한칸
# 문자열을 입력받아 키로거가 입력한 순서대로 화면에 출력
t = int(input())
for _ in range(t):
  left = deque()
  right = deque()
  data = input().rstrip()
  for key in data:
    if key == '-':
      if left:
        left.pop()
    elif key == '<':
      if left:
        right.appendleft(left.pop())
    elif key == '>':
      if right:
        left.append(right.popleft())
    else:
      left.append(key)
  left.extend(right)
  print(''.join(left))