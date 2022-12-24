# 1보다 크고 n보다 작같아 같은 모든 자연수로 나누어 떨어지는 수
# 영식이와 다솜이 n이 주어질때 그 수가 뭔지 구하기
# 987654321로 나눈 나머지를 출력
# n은 1000000보다 작거나 같은 자연수이다.
n = int(input())
nums = [False for _ in range(10**6+1)]
# 확인한 수인지 확인

result = 1
for i in range(2,n+1):
    if nums[i]:
        continue
    t = 1
    for j in range(i,n+1,i):
        # i의 배수는 다시 갈 필요 없으므로
        nums[j] = True
        tmp = j
        cnt = 0
        # 몇 배수인지 확인
        while tmp > 1 and tmp % i == 0:
            tmp //= i
            cnt += 1
        t = max(t,cnt)
    for _ in range(t):
        result = (result*i) % 987654321
print(result)