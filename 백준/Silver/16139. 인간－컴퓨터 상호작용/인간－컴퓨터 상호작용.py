import sys
# 16139 인간 - 컴퓨터 상호작용
input = sys.stdin.readline

S = list(input().rstrip())
T = int(input())
cache = list([] for _ in range(ord('z')-ord('a')+1))
data = [0]*(ord('z') - ord('a')+1)

for i in range(len(S)):
  data[ord(S[i])-ord('a')] += 1
  for j in range(ord('z')-ord('a')+1):
    cache[j].append(data[j])

result = []

for t in range(T):
  s, start, end = input().rstrip().split()
  s = ord(s) - ord('a')
  start = int(start)
  end = int(end)
  if start == 0:
    result.append(cache[s][end])
  else:
    result.append(cache[s][end] - cache[s][start-1])
for i in result:
  print(i)