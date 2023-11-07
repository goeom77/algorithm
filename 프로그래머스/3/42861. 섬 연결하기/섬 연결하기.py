from heapq import heappush,heappop
def solution(n, costs):
#   n개 섬에 코스트
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    answer = 0
    def getParent(n):
        if parent[n] == n:
            return n
        parent[n] = getParent(parent[n])
        return parent[n]
    def unionParent(a,b):
        a = getParent(a)
        b = getParent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    def unionFind(a,b):
        a = getParent(a)
        b = getParent(b)
        if a == b:
            return True
        return False
    for cost in costs:
        if not unionFind(cost[0],cost[1]):
            unionParent(cost[0],cost[1])
            answer += cost[2]
    return answer