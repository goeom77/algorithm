# n개의 막대기둥 폭은 1미터
# 기둥을 이용해 창고제작 모두 사용해야된다.
# 지분의 수평부분은 반드시 어떤 기둥의 윗면에 닿아야한다. 지분이 아니라 지붕이야 바보
# 지붕의 수직부분은 반드시 어떤 기둥의 옆면에 닿아야한다.
# 비가올때 고이지 않게 오목 x
# 창고 다각형의 면적이 가장 작게
# 가장 높은 것을 기준으로 낮아져야한다.
# 케이스의 개수
case = int(input())
arr = [0]*1001
mx_h = 0
mx_h_x = 0
mx_x = 0
for i in range(case):
    x, h = map(int,input().split())
    if h > mx_h:
        mx_h = h
        mx_h_x = x
    if x > mx_x:
        mx_x = x
    arr[x] = h
# L과 H 둘다 1~1000
rh = lh = 0
for i in range(mx_h_x):
    # mx_h_x 전까지 높이를 고정한다.
    if rh < arr[i]:
        rh = arr[i]
    arr[i] = rh
for j in range(mx_x,mx_h_x,-1):
    if lh < arr[j]:
        lh = arr[j]
    arr[j] = lh
total = 0
for k in range(mx_x+1):
    total += arr[k]
print(total)