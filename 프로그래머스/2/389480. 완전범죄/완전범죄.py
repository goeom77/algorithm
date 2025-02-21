def solution(info, n, m):
    dp = set()
    dp.add((0, 0))  # 초기 상태

    for trace_a, trace_b in info:
        next_dp = set()
        for a, b in dp:
            if a + trace_a < n:
                next_dp.add((a + trace_a, b))
            if b + trace_b < m:
                next_dp.add((a, b + trace_b))
        
        dp = next_dp  # 업데이트된 상태를 반영
    print(dp)
    if dp:
        for a, b in sorted(dp):
            return a

    return -1
