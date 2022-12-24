import sys
ssr = sys.stdin.readline

def func(N, n, max_len, num_cnt):
    if n == max_len:
        return N
    
    num_cnt[int(N[max_len - 1 - n])] += 1
    s = ''
    for i in range(9, -1, -1):
        s += str(i) * num_cnt[i]
    if N[-1 - n:] == s:
        return func(N, n + 1, max_len, num_cnt)
    
    s = ''
    for i in range(int(N[-1 - n]) + 1, 10):
        if num_cnt[i] > 0:
            s += str(i)
            num_cnt[i] -= 1
            break
    for i in range(10):
        s += str(i) * num_cnt[i]
    return N[:-1 - n] + s

T = int(ssr())
for _ in range(T):
    num_cnt = [0 for _ in range(10)]
    N = ssr()[:-1]
    
    max_len = len(N)
    s = func(N, 0, max_len, num_cnt)
    
    if s == N:
        print("BIGGEST")
    else:
        print(s)