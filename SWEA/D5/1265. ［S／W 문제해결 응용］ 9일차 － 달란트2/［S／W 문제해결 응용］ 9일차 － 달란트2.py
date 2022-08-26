# 달란트 시장을 연다
# 칭찬 -> 1달란트 -> 1년동안 -> 사탕
# 10달란트 주면 10개 3묶음으로 나눠 각 묶음의 곱으로 준다.
# 달란트 수, 묶음 수
T = int(input())
for t in range(1,T+1):
    d, num = map(int, input().split())
    total = 0
    a = d // num
    arr = [a for _ in range(num)]
    b = d % num
    result = 0
    if b == 0:
        result = a**num
    else:
        for i in range(b):
            arr[i] += 1
    total = 1
    for i in range(len(arr)):
        total *= arr[i]
    print(f'#{t} {max(result,total)}')