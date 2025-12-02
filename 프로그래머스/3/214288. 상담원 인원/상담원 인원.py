from heapq import heappush, heappop
def solution(k, n, reqs):
    # k개의 상담유형, n명의 상담사, 상담사는 상담유형 하나만 가능 최소 대기 시간의 합은?
    cnt_n = [1]*(k) # 타입을 k-1로 줄임
    req = [[] for _ in range(k)]
    extra_n = n-k
    delay = [0]*(k)
    for (a,b,c) in reqs:
        req[c-1].append((a,b))

    # 기존의 delay와 인원 늘렸을때 delay의 차이가 많이 발생하는 곳 한군데 줄일것
    # 1일때 delay 계산
    def calcurate(people, k):
        delay = 0
        time = []
        for i in range(people):
            heappush(time,0)
        for start_time, duration in req[k]:
            now = heappop(time)
            if now <= start_time:
                heappush(time,start_time + duration)
            else:
                delay += now - start_time
                heappush(time,now + duration)
        return delay
    for i in range(k):
        if len(req[i]) == 0:
            continue
        delay[i] = calcurate(1,i)
    
    while extra_n > 0:
        tmp_delay = [0]*(k)
        tmp_index = -1
        tmp_max = -1
        for i in range(k):
            if len(req[i]) == 0:
                continue
            tmp_delay[i] = calcurate(cnt_n[i]+1,i)
            if tmp_max < delay[i] - tmp_delay[i]:
                tmp_max = delay[i] - tmp_delay[i]
                tmp_index = i
        extra_n -= 1
        delay[tmp_index] = tmp_delay[tmp_index]
        cnt_n[tmp_index] += 1
        
    
    print(delay)
    
    answer = sum(delay)
    
    return answer