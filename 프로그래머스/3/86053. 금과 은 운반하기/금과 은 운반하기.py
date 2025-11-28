from heapq import heappush, heappop
def solution(a, b, g, s, w, t):
    left = 0
    right = 10**15
    while (left <= right):
        T = (right + left) // 2
        goldAvailable = False
        silverAvailable = False
        totalAvailable = False
        
        cnt = [0] * len(t)
        for i in range(len(t)):
            k = T // (2*t[i])
            if T % (2*t[i]) >= t[i]: 
                k += 1
            cnt[i] = k
        tmpMax = 0
        tmpGold = 0
        tmpSilver = 0
        for i in range(len(t)):
            amount = cnt[i]*w[i]
            tmpGold += min(g[i],amount)
            tmpSilver += min(s[i],amount)
            tmpMax += min(g[i]+ s[i], amount)
        if tmpGold >= a:
            goldAvailable = True
        if tmpSilver >= b:
            silverAvailable = True            
        if goldAvailable and silverAvailable:
            if tmpMax >= a + b:
                totalAvailable = True
        if totalAvailable:
            right = T-1
        else:
            left = T+1
    answer = left
    return answer