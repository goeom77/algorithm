import sys
input = sys.stdin.readline
n, m = map(int, input().split())
intToStringDict = {}
stringToIntDict = {}
for c in range(1,n+1):
    # c가 숫자인가
    value = input().strip()
    intToStringDict[c] = value
    stringToIntDict[value] = c
for _ in range(m):
    test = input().strip()
    if test.isdigit():
        print(intToStringDict[int(test)])
    else:
        print(stringToIntDict[test])