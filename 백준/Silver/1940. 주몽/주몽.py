# 재료는 고유번호가지고있다.
# 고유번호의 합이 M이 되면 1~1000000 갑옷 제작
import sys
n = int(input())
m = int(input())
number = list(map(int,sys.stdin.readline().split())) # 고유하다.
number.sort()
if n == 1:
    print(0)
else:
    mid = 0
    for i in range(len(number)):
        if number[i] > m//2:
            mid = i
            break
    cnt = 0
    s_p = mid - 1
    e_p = mid
    while s_p >= 0 and e_p < n:
        if number[s_p] + number[e_p] == m:
            cnt += 1
            s_p -= 1
            e_p += 1
        elif number[s_p] + number[e_p] < m:
            e_p += 1
        else:
            s_p -= 1
    print(cnt)