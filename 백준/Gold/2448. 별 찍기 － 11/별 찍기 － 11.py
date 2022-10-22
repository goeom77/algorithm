n = int(input())
# 3의 배수 로 나온다.
arr = [0]+[[0]*(2*n-1) for _ in range(n)]

def triangle(i,j,n):
    if n==3:
        arr[j-1][i+1] = '*'
        arr[j-1][i+3] = '*'
        arr[j-2][i+2] = '*'
        for k in range(5):
            arr[j][i+k] = '*'
        return
    else:
        triangle(i,j,n//2)
        triangle(i+n,j,n//2)
        triangle(i+n//2,j-n//2,n//2)

triangle(0,n,n)
for j in range(1,n+1):
    for i in range(2*n-1):
        if arr[j][i] == 0:
            print(' ',end='')
        else:
            print(arr[j][i],end='')
    print()
      
        