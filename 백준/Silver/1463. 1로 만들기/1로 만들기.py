import sys

n = int(sys.stdin.readline())

result = [n] * (n+1)
result[n] = 0

for i in range(n,1,-1):
    if i % 3 == 0:
        result[i//3] = min(result[i//3],result[i] + 1)
    if i % 2 == 0:
        result[i//2] = min(result[i//2],result[i] + 1)

    result[i-1] = min(result[i-1],result[i]+1)

print(result[1])