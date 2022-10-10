'''
0은 빈 칸, 1은 집, 2는 치킨집을 의미한다.
집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다.
치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
'''

def chicken_len(h, c):
    return abs(h[0]-c[0]) + abs(h[1]-c[1])

from itertools import combinations
import sys
# input = sys.stdin.readline


n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

map_dict = {1:[], 2:[]}
for i in range(n):
    for k in range(n):
        if ground[i][k]:
            map_dict[ground[i][k]].append([i, k])

all_len = [[] for _ in range(len(map_dict[1]))]

for i, h in enumerate(map_dict[1]):
    for c in map_dict[2]:
        all_len[i].append(chicken_len(h, c))

for_combi = [i for i in range(len(map_dict[2]))]
combi = combinations(for_combi, m)

result = float('inf')
for co in combi:
    tmp_result = 0

    for i in all_len:
        tmp_len = []
        for c in co:
            tmp_len.append(i[c])
        tmp_result += min(tmp_len)
        if tmp_result >= result:
            break

    if tmp_result < result:
        result = tmp_result

print(result)