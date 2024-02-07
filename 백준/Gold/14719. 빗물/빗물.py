import sys

input = sys.stdin.readline
# 14719 빗물
# 빗물이 고이는 총량을 구하기
# 낮아졌다가 높아지면 그 양쪽 사이 낮은 벽만큼 물이 고이게 된다.
result = 0
h, w = map(int, input().split()) # 세로, 가로
arr = list(map(int, input().split()))
for i in range(1, w-1):
  left = max(arr[:i])
  right = max(arr[i+1:])
  min_height = min(left, right)
  if min_height > arr[i]:
    result += min_height - arr[i]
print(result)