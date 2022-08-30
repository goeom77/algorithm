import sys
input = sys.stdin.readline

n = int(input())
result = []


for i in range(n):
    order = list(input().split())

    if order[0] == 'push':
        result.append(order[1])

    elif order[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            tmp = result.pop()
            print(tmp)

    elif order[0] == 'size':
        print(len(result))

    elif order[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    
    elif order[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
