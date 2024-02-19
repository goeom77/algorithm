import sys
input = sys.stdin.readline

input = sys.stdin.readline
# 1679 숫자 놀이
# 상대보다 1큰 숫자를 만들어야 한다.
# 한숫자는 최대 k번 사용가능
# holsoon, jjaksoon 순으로 게임진행 이기면 name win at 숫자로 return
# 1 = 1
# 2 = 1 1
# 3 = 1 1 1
# 4 = 1 3
# 5 = 1 1 3
# 6 = 1 1 1 3
# 7 = 1 3 3
# 8 = 1 1 3 3 
# 9 = 3 3 3
# 10 = 1 3 3 3
# 11 = 1 1 3 3 3
# 12 = 3 3 3 3
# 13 = 1 3 3 3 3
# 14 = 1 1 3 3 3 3 -> 6개 사용했으므로 답
N = int(input())
num = list(map(int, input().split()))
k = int(input())

s = 0
tmp = 0
while True:
  tmp += 1
  s = tmp
  cnt = 0
  for i in range(len(num)-1,-1,-1):
    if num[i] == 1:
      cnt += s
      s = 0
      break
    if (s == 0): break
    if num[i] <= s:
      cnt += s//num[i]
      s %= num[i]
  if s != 0 or cnt > k:
    break
if tmp % 2 == 0:
  print("holsoon win at",tmp)
else:
  print("jjaksoon win at",tmp)