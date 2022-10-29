def aaa(n):
    if n != '.':
        print(n, end='')
        aaa(dic[n][0])
        aaa(dic[n][1])
    print('',end='')


def bbb(n):
    if n != '.':
        bbb(dic[n][0])
        print(n, end='')
        bbb(dic[n][1])
    print('',end='')


def ccc(n):
    if n != '.':
        ccc(dic[n][0])
        ccc(dic[n][1])
        print(n, end='')
    print('',end='')


N = int(input())
dic = {}
for _ in range(N):
    x, y, z = input().split()
    dic[x] = [y, z]

aaa('A')
print()
bbb('A')
print()
ccc('A')