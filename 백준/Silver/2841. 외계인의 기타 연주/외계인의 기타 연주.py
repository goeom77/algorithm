import sys

input = sys.stdin.readline
# 2841번 외계인의 기타 연주
# 6개 줄이 있다면 여러개중 가장 높은 프렛이 음을 발생한다.
# 손가락은 수십억개이다.(외계인이니까)
N, P = map(int, input().split())
stack = [[] for _ in range(7)]
# 줄은 6개
cnt = 0
for _ in range(N):
    line, fret = map(int, input().split())
    # 줄이 비어있으면 그냥 넣는다.
    if not stack[line]:
        stack[line].append(fret)
        cnt += 1
        continue
    # 줄이 비어있지 않으면
    # 높은 프렛이면 그냥 넣는다.
    if stack[line][-1] < fret:
        stack[line].append(fret)
        cnt += 1
        continue
    # 낮은 프렛이면
    # 같은 프렛이면 무시한다.
    if stack[line][-1] == fret:
        continue
    # 같은 프렛이 나올때까지 pop한다.
    while stack[line] and stack[line][-1] > fret:
        stack[line].pop()
        cnt += 1
    # 같은 프렛이 나오면 무시한다.
    if stack[line] and stack[line][-1] == fret:
        continue
    # 같은 프렛이 나오지 않으면 넣는다.
    stack[line].append(fret)
    cnt += 1
print(cnt)

