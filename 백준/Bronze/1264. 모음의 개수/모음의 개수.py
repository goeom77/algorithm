while True:
    a = input()
    if a == '#':
        break
    aa = ['a','A','e','E','i','I','u','U','o','O']
    cnt = 0
    for j in range(len(a)):
        if a[j] in aa:
            cnt += 1
    print(cnt)