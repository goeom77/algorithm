import sys
input = sys.stdin.readline
test = int(input())
for t in range(test):
    n = int(input())
    clothes = {}
    for i in range(n):
        name , kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    result = 1
    for i in clothes:
        result *= (clothes[i]+1)
    print(result-1)