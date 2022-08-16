import sys
T = int(sys.stdin.readline().rstrip())
stack = []
order = []
for t in range(T):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())
    else:
        if len(stack) == 0:
            print('1')
        else:
            print('0')