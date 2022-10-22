# 종이의 개수
minus = 0
zero = 0
plus = 0
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
def counter(i,j,k):
    global minus
    global zero
    global plus
    cnt = arr[j][i]
    ck = 0
    if k != 1:
        for dj in range(k):
            for di in range(k):
                if arr[j+dj][i+di] != cnt:
                    ck = 1
                    break
            if ck:
                break
    if ck:
        for ni in range(3):
            for nj in range(3):
                counter(i+ni*(k//3),j+nj*(k//3),k//3)
    else:
        if cnt == -1:
            minus += 1
        elif cnt == 0:
            zero += 1
        else:
            plus += 1
counter(0,0,n)
print(minus)
print(zero)
print(plus)

