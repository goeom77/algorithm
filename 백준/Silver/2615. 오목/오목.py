import sys
input = sys.stdin.readline
# 2615 오목
# 검정은 1, 흰색은 2
graph = [list(map(int, input().split())) for _ in range(19)]
# 5개 연속이면 해당 색깔이 이기는 것
# 결과는 이긴 숫자
# 이기게 만든 바둑알 중 가장 왼쪽 위의 바둑알 가로번호, 세로번호 출력
result = False
for j in range(19):
  for i in range(19):
    if graph[j][i] == 0:
      continue
    for di,dj in [(1,0),(0,1),(1,1),(1,-1)]:
      if 0 <= i+4*di < 19 and 0 <= j+4*dj < 19:
        if graph[j][i] == graph[j+dj][i+di] == graph[j+2*dj][i+2*di] == graph[j+3*dj][i+3*di] == graph[j+4*dj][i+4*di]:
          if 0 <= i+5*di < 19 and 0 <= j+5*dj < 19:
            if graph[j][i] == graph[j+5*dj][i+5*di]:
              continue
          if 0 <= i-di < 19 and 0 <= j-dj < 19:
            if graph[j][i] == graph[j-dj][i-di]:
              continue
          print(graph[j][i])
          print(j+1,i+1)
          result = True
          break
if not result:
  print(0)