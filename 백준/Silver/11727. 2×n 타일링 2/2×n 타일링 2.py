# print(divmod(a,2)) # (2,1)
# 앞에 것은 (세로 2개, 가로 2개, 큰거 1개로 case가 3개가 된다.)
# 뒤에 것은 a *2 개만큼 경우의 수가 생긴다.

case = int(input())
data = divmod(case,2) # 몫과 나머지 산출
result = 0
cnt = 1
n = data[0]
if data[1] == 0:
    while n != 0:         # 나머지가 0인 경우
        cnt = cnt * 4 - 1 # 경우의 수 + 1 (세로 1칸짜리의 경우 서로 겹치므로)
        n -= 1

else:                     # data[1] == 1
    while n != 0:         # 나머지가 1인 경우
        cnt = cnt * 4 + 1 # 경우의 수 - 1 (세로 1칸짜리의 경우 서로 겹치므로)
        n -= 1

print(cnt%10007)

