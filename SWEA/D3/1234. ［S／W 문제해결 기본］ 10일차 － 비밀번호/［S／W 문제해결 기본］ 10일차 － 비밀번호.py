for t in range(1,11):
    long, arr = input().split()
    stack=[]
    stack.append(arr[0])
    for i in range(1, int(long)):
        if len(stack) == 0:
            stack.append(arr[i])
        elif arr[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(arr[i])
    print(f'#{t}',end=" ")
    print(*stack,sep="")