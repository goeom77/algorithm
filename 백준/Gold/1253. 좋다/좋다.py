import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = 0
arr.sort()
# 이분탐색
for k in range(n):
    # 다른 2개의 수의 합으로 만들어진 합이니깐 index로 접근
    # 숫자가 같아도 되니깐 index로 접근해도 괜찮다.
    find = arr[k]
    i = 0
    j = n-1
    while i < j:
        if arr[i] + arr[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif arr[i] + arr[j] < find:
            i += 1
        else:
            j -= 1
print(result)