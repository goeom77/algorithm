# 보안시스템 설치
# 서로다른 L개 소문자로 구성 = 최소 한개 모음(aeiou) 최소 두개 자음으로 구성
# 사전 순으로 배열
def comb(n,m,j):
    if n == m:
        cnt = 0
        for i in chosen:
            if i in collection:
                cnt += 1
        if 1<= cnt < M-1:
            print(*chosen,sep='')
    else:
        for i in range(j,len(arr)):
            chosen[n] = arr[i]
            comb(n+1,m,i+1)

M,N = map(int, input().split()) # l개 암호, c개 중에서
arr = list(input().split())
arr.sort()
collection = ['a','e','i','o','u']

# 모음 한개, 자음 두개를 지정하고 L-3을 선택하면 된다.


chosen = [0] * M
comb(0,M,0)
