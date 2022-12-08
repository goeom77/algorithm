import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
result = 0
# 병합정렬
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:] # 일정 이하로 0개가 되면 안더해지니깐
    merged_arr += high_arr[h:]
    return merged_arr
arr = merge_sort(array)
# print(arr)
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