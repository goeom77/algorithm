# 별찍기 - 10
# n만큼 패턴 반복
n = int(input())
t = n
arr = [[0]*n for _ in range(n)]
n //= 3
a = 0
b = 0
def pattern(a,b,n):
    global arr
    if n == 1:
        for ii in range(3):
            for jj in range(3):
                if ii != 1 or jj != 1:
                    ai = a + ii
                    bj = b + jj
                    arr[bj][ai] = 1
        return
    else:
        m = n//3
        for i in range(0,3*n,n):
            for j in range(0,3*n,n):
                if j != n or i != n:
                    ai = a + i
                    bj = b + j
                    arr[bj][ai] = 1
        return pattern(a,b,m), pattern(a+n,b,m), pattern(a+2*n,b,m),pattern(a,b+n,m),pattern(a,b+2*n,m),pattern(a+2*n,b,m),pattern(a+n,b+2*n,m),pattern(a+2*n,b+2*n,m),pattern(a+2*n,b+n,m)
pattern(a,b,n)
for j in range(t):
    for i in range(t):
        if arr[j][i]== 1:
            arr[j][i] = "*"
        else:
            arr[j][i] = ' '
for i in range(t):
    print(*arr[i],sep='')



