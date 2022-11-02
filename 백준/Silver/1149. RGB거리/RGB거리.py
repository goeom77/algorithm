nx = {0:[1,2], 1:[0,2], 2:[0,1]}

hold = [0,0,0]

N = int(input())
for i in range(N):
  cost = [int(x) for x in input().split()]
  for j in range(3):
    cost[j]+=min(hold[nx[j][0]], hold[nx[j][1]])
  hold = cost

print(min(cost))