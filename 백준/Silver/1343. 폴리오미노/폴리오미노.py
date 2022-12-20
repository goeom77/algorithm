# 폴리오미노 2개 무한개 가지고 있다. 'AAAA''BB'
# x는 폴리오미노 .은 패스
# n 최대 크기 50
import sys
input = sys.stdin.readline

storage = list()
getinput = input().rstrip()
arr = list(getinput.split('.'))
getinput = list(getinput)
flag = True
result = ''
for i in range(len(arr)):
    tmpLen = len(arr[i])
    a = tmpLen // 4
    tmpLen %= 4
    b = tmpLen //2
    tmpLen %= 2
    if tmpLen > 0:
        flag = False
    else:
        if (a,b) == (0,0):
            continue
        else:
            storage.append((a,b))

cnt = 0
resultflag = True
if flag:
    for i in range(len(getinput)):
        if resultflag==True and getinput[i] == 'X':
            a,b = storage[cnt]
            result += 'AAAA'*a
            result += 'BB'*b
            resultflag = False
            cnt += 1
        elif getinput[i] == '.':
            result += '.'
            resultflag = True
    print(result)
else:
    print('-1')