import sys;
input = sys.stdin.readline

while True:
    ck = 0
    n = int(input())
    if n:
        a = str(n)
        for i in range(len(a)//2):
            if a[i] != a[len(a) -1 - i]:
                ck = 1
                break
        if not ck:
            print('yes')
        else:
            print('no')
    else:
        break