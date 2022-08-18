a,b = map(int,input().split())
cnt = 1
for i in range(1,a+1):
    cnt *= i
for j in range(1,b+1):
    cnt //= j
c = a-b
for k in range(1,c+1):
    cnt //= k
print(cnt)