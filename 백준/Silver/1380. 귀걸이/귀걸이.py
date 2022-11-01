# 빨간 귀걸이 압수
# 뒤에 여학생 번호, a,b적기
t = 0
while True:
    t+= 1
    n = int(input())
    if n== 0:
        break
    name = []
    for i in range(n):
        name.append(input())
    arr = [0]*(n+1)
    for j in range(2*n-1):
        idx, r = input().split()
        idx = int(idx)
        if arr[idx] == 0:
            arr[idx] = 1
        else:
            arr[idx] = 0
    print(t,end=' ')
    for j in range(1,n+1):
        if arr[j] == 1:
            print(name[j-1])