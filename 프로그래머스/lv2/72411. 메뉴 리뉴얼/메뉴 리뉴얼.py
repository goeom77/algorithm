def solution(orders, course):
    # 기존 단품 중 같이 주문한 메뉴 조합해서 새로운 메뉴 제공 2~20가지 종류
    # 최소 2가지, 최소 2명이상 손님이 주문한 조합
    # course의 수는 조합 개수 2~10
    # [조합, 주문횟수] 으로 넣기
    new_menu = [[] for _ in range(11)] # course마다 가능 메뉴 10까지만 가능
    new_menu_count = {} # munu들의 count
    def comb(order,n,m,j): # 조합하기
        if n == m:
            str_chosen = ''.join(s for s in chosen[:])
            if str_chosen in new_menu[m]:
                new_menu_count[str_chosen] += 1
                return
            else:
                new_menu[m].append(str_chosen) # new_menu의 길이 m 중에 조합가능 메뉴
                new_menu_count[str_chosen] = 1
                return
        else:
            for i in range(j,len(order)):
                chosen[n] = order[i]
                comb(order,n+1,m,i+1)
                chosen[n] = 0 # 이게 있어야지만 백트래킹을 하는 걸까?
    for count in course: # 코스의 개수 count 1~10
        for order in orders:
            chosen = [0]*count
            order = list(order)
            order.sort()
            comb(order,0,count,0)
    result = []
    min_course_num = [0 for _ in range(11)]
    for i in course:
        tmp = []
        for case in new_menu[i]:
            if new_menu_count[case] > 1:
                tmp.append([-new_menu_count[case],case])
                if -new_menu_count[case] < min_course_num[i]:
                    min_course_num[i] = -new_menu_count[case]
        tmp.sort()
        for j in tmp:
            if j[0] == min_course_num[i]:
                result.append(j[1])
    result.sort()
            
    answer = result
    return answer