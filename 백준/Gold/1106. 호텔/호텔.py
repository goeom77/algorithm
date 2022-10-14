INF= int(1e7)
c, n = map(int, input().split())
# 달성할 고객 수 c 도시개수 n

data = []
mx_people = 0
for i in range(n):
    money, people = map(int, input().split())
    if mx_people < people:
        mx_people = people
    data.append((money, people))
dp = [INF]*(c+1+mx_people)
dp[0] = 0 # 기본값
for j in range(len(data)):
    for i in range(c+mx_people):#  오름차순을 통한 배수 값 입력 -> 중복은 어떻게 막지?(가장 싼걸로 들어가니깐 막을 필요 x)
        if dp[i] != INF:
            if i + data[j][1] > c+mx_people: # dp 범위를넘어간 경우
                break
            dp[i + data[j][1]] = min(dp[i] + data[j][0],dp[i + data[j][1]])
tmp = INF
for i in range(mx_people):
    if dp[c+i] < tmp:
        tmp = dp[c+i]
print(tmp)
        



