import sys

T = int(sys.stdin.readline().rstrip())
arr = []
for t in range(T):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
for i in range(T):
    print(arr[i])