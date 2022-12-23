# 문제 : 정수 N과 K가 주어졌을 때, 다음 두 조건을 만족하는 문자열 S를 찾는 프로그램을 작성하시오.

# 1. 문자열 S의 길이는 N이고, 'A', 'B'로 이루어져 있다.
# 2. 문자열 S에는 0 ≤ i < j < N 이면서 s[i] == 'A' && s[j] == 'B'를 만족하는 (i, j) 쌍이 K개가 있다.

# 해석
# n, k 주어질 때 두조건 만족하는 s문자열 찾기
# 1. s 길이는 n이고 'A' ,'B'로 구성
# 2. 0<= i < j < n 이면서 s[i] = 'A', s[j] = 'B' 만족하는 i,j쌍이 k개 있다.

n, k = map(int, input().split())
idx = 0
res = []  #len(res) a의 개수 , a의 인덱스
cnt = 0
bcnt = n - 1  # b의 개수
for i in range(n):
    if cnt == k:
        break
    cnt -= len(res)  #a가 한개 들어가므로 쌍의 개수가 1개씩 사라짐
    bcnt -= 1  #a가 들어가므로 b의 개수가 줄어듬
    for j in range(n, idx, -1):
        if cnt + n - j == k: #k개의 쌍이 만들어지면 종료
            idx = j #사실 의미없는줄..
            res.append(j) # res에 A가 들어가는 인덱스
            cnt += n - j #만들수있는지 체크하기위해서 cnt를 넣어줌
            break
        if idx == j - 1 and cnt + n - j <= k:
            idx = j
            res.append(idx)
            cnt += n - j
        elif cnt + n - j < k:
            continue
        elif cnt + n - j > k:
            idx = j + 1
            cnt += n - j - 1
            res.append(j + 1)
            break
if cnt != k:
    print(-1)
else:
    ans = ''
    for i in range(1, n + 1):
        if i in res:
            ans += 'A'
        else:
            ans += 'B'
    print(ans)