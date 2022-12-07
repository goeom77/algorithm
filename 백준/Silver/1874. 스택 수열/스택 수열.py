import sys

T = int(input())
stack = []
goal = []
for i in range(T):
    goal.append(sys.stdin.readline().strip())

idx = 0
num = 1
result = []
while True:
    if idx == T:
        break
    elif goal[idx] not in stack:
        stack.append(str(num))
        num += 1
        result.append('+')
    elif goal[idx] == stack[-1]:
        stack.pop()
        idx += 1
        result.append('-')
    else:
        result = ['NO']
        break

for i in range(len(result)):
    print(result[i])