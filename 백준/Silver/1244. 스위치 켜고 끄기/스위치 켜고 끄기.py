# 1부터 n 까지 스위치
# 1은 켜져있고 0은 꺼져있다.
# 남학생은 자기 받은 수의 배수이면 바꾸고
# 여학생은 자신 주위 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아 바꾼다.
# 이때 스위치 개수는 홀수가 된다.
# 스위치 개수
n = int(input())
# 스위치 상태
switch = [0] + list(map(int, input().split()))
# 학생수
num = int(input())
# x = 1 남 2 여 : 받은 순번
arr = []
for i in range(num):
    x, b = map(int, input().split())
    arr.append([x, b])
# x를 확인하고 하는 방법을 다르게 한다. 사람수만큼
for i in range(num):
    if arr[i][0] == 1:
        c = arr[i][1]
        for j in range(c, n + 1, c):
            switch[j] = (switch[j] + 1) % 2
    else:
        a = arr[i][1]
        switch[a] = (switch[a] + 1) % 2
        cnt = 1
        while True:
            # a +- cnt 가 스위치 개수안에 있으면 그것을 비교한다.
            if a + cnt <= n and a - cnt > 0:
                if switch[a + cnt] == switch[a - cnt]:
                    switch[a + cnt] = switch[a - cnt] = (switch[a + cnt] + 1) % 2
                    cnt += 1
                else:
                    break
            else:
                break
switch.pop(0)

for i in range(n):
    if i % 20 == 19:
        print(switch[i])
    else:
        print(switch[i], end=' ')