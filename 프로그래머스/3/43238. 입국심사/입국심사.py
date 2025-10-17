def solution(n, times):
    answer = 0
    left = 0
    right = max(times)*n//len(times)
    while (left <= right):
        total = 0
        mid = (left + right) // 2
        for time in times:
            total += (mid // time)
            # if total > n:
            #     break
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
                
    return answer