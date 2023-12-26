import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
graph = list(map(int,input().split())) 

max_ans = float('-inf')

for i in permutations(graph):
  ans = 0
  for j in range(n-1):
    ans += abs(i[j] - i[j+1])
  max_ans = max(max_ans,ans)

print(max_ans)