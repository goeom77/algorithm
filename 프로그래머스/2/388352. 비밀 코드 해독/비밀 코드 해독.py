from itertools import combinations
def solution(n, q, ans):
    # 1~10,30 까지의 정수 중 5가지 선택할 수 있는 방법
    # 30 C 5 = 29*28*27*4 = 100000가지?를 5번씩 -> 50만번
    num = list(i for i in range(1,n+1))
    arr = []
    for i in combinations(num,5):
        arr.append(i)
    checklist = [True]*len(arr)
    for i in range(len(arr)):
        for j in range(len(q)):
            tmp = 0
            for k in range(5):
                if q[j][k] in arr[i]:
                    tmp += 1
            if tmp != ans[j]:
                checklist[i] = False
                break
    
    answer = sum(checklist)
    return answer