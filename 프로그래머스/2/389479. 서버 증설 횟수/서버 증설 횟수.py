def solution(players, m, k):
    # players + m >= m * room > players
    # k시간 유지
    # 최소 방 개설 횟수 출력
    q = [0]*len(players)
    answer = 0
    day = 0
    for player in players:
        if int(player/m) > q[day]:
            add_value = int(player/m) - q[day]
            # 각 날짜에 추가하기
            for i in range(k):
                if (day + i) >= len(players):
                    break
                q[day+i] += add_value
            answer += add_value
        day += 1
    return answer