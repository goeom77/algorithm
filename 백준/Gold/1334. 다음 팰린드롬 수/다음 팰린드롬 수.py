import sys
input = sys.stdin.readline

N = int(input().rstrip()) +1
str_N = str(N)
l = len(str_N)//2
real_l = len(str_N)
complete = list(int(i) for i in str_N)
if real_l == 1:
    print(N)
else:     
    for i in range(l):
        if complete[i] < complete[real_l-1-i]:
            complete[real_l-2-i] += 1
        complete[len(str_N)-1-i] = complete[i]
    for i in range(real_l-1,-1,-1):
        if complete[i] > 9:
            complete[i] = 0
            complete[i-1] += 1
    for i in range(l):
        complete[real_l-1-i] = complete[i]
    result = ''
    for i in complete:
        result += str(i)
    print(result)

