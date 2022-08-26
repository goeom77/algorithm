# 아래부터 주사위를 쌓는다.
# 규칙은 서로 붙어있는 두개의 주사위에서 아래 주사위의 위는 위 주사위의 아랫면과 일치
# 4개의 옆면에서 한면의 숫자의 합이 최대가 되도록 쌓게 할 때 한 옆면의 숫자의 합의 최댓값은??
# 0-5 / 1-3/ 2-4 세트
num = int(input())
arr = []
for i in range(num):
    arr.append(list(map(int,input().split())))
fb = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
# 주사위 원하는 면의 idx가 일치하는 fb의 idx를 넣고 비교
# 1주사위의 밑면과 일치하는 숫자
result = 0
# 주사위 리스트
# 주사위 6개 면 전부 확인 위에 면을 한개로 고정
for b in range(1,7):
    max_sum = 0
    # 첫번째 주사위 top 구하기
    t = arr[0][fb[arr[0].index(b)]]
    cnt = 1
    for j in range(6, 0, -1):
        if j != b and j != t:
            max_sum += j
            break
    # 두번째 ~ num번째 주사위 bottom과 top구하기
    while cnt < num:
        bb = t
        t = arr[cnt][fb[arr[cnt].index(bb)]]
        for j in range(6, 0, -1):
            if j != bb and j != t:
                max_sum += j
                break
        cnt += 1


    # 주사위 다 더함
    if max_sum > result:
        result = max_sum

print(result)