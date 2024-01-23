import sys

input = sys.stdin.readline
# 1105 팔
L, R = map(str, input().split())
ans = 0
if L == R:
    for i in range(len(L)):
        if L[i] == '8':
            ans += 1
    print(ans)
elif len(R) - len(L) >= 1:
  print(0)
else:
    for i in range(len(L)):
        if L[i] != R[i]:
            break
        if L[i] == '8':
            ans += 1
    print(ans)