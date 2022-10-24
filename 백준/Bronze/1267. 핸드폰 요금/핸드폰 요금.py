n = int(input())
arr = list(map(int, input().split()))
y = 0
m = 0
for i in range(n):
    y+= (arr[i] // 30) * 10+10
    m += (arr[i]//60) * 15+15
if y > m:
    print('M', m)
elif y == m:
    print('Y','M', m)
else:
    print('Y', y)