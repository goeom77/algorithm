a, b = map(int, input().split())
cnt = [0,0]
while True:
    if a == b == 1:
        break
    if a > b:
        if b == 1:
            tmp = a-b
            cnt[0] += tmp
            a = 1
        else:
            tmp = a // b
            cnt[0] += tmp
            a %= b
    else:
        if a == 1:
            tmp = b-a
            cnt[1] += tmp
            b = 1
        else:
            tmp = b // a
            cnt[1] += tmp
            b %= a
print(*cnt)
