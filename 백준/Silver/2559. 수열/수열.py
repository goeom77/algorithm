import sys
input = sys.stdin.readline
# 2559 연속된 수열
n, k = map(int, input().split())
# n 숫자 개수 k 연속된 수
arr = list(map(int, input().split()))
tmp = 0
for i in range(k):
  tmp += arr[i]
maxValue = tmp
for i in range(k,n):
  tmp += (arr[i] - arr[i-k])
  maxValue = max(maxValue, tmp)
print(maxValue)