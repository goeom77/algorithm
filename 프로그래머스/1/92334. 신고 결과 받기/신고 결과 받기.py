def solution(id_list, report, k):
    reporter = {} # 내가 신고한 사람
    reportMe = {} # 나를 신고한 사람
    for id in id_list:
        reporter[id] = set()
        reportMe[id] = set()

    ban = []
    for value in set(report):
        re, banner = value.split()
        reporter[re].add(banner)
        reportMe[banner].add(re)
        if len(reportMe[banner]) == k:
            ban.append(banner)
    # 내가 신고한 사람중 몇명이 ban되었는지 list cnt를 보여주기
        
    # ban된 유저
    answer = [0]*len(id_list)
    for i in range(len(id_list)):
        for j in reporter[id_list[i]]:
            if j in ban:
                answer[i] += 1
    return answer