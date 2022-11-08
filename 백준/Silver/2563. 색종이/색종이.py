import sys
input = sys.stdin.readline
n = int(input())
arr = [[0]*100 for _ in range(100)]
for t in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[b+j][a+i] = 1
total = 0
for i in range(100):
    for j in range(100):
        total += arr[j][i]
print(total)
    