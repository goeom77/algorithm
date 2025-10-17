def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    rocks.append(distance)
    left,right = 1, distance

    while left <= right:
        prev = 0
        removed = 0
        mid = (left + right) // 2
        
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
            else:
                prev = rock
        if removed > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
            
            
        
    
    return answer