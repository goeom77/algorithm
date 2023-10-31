from collections import defaultdict
def solution(participant, completion):
    # 완주하지 못한 사람 return 동명이인 있으면 한명씩 감소
    name = defaultdict(int)
    nameList = []
    for i in participant:
        name[i] += 1
        if(name[i] == 1):
            nameList.append(i)
        
    for i in completion:
        name[i] -= 1
    for i in nameList:
        if name[i] == 1:
            return i

    return ''