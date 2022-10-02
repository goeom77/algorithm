# 세 수
# 숫자 세개로 이루어진 등식을 적음
a,b,c = map(int, input().split())

if a + b == c:
    print(f'{a}+{b}={c}')
elif a - b == c:
    print(f'{a}-{b}={c}')
elif a*b == c:
    print(f'{a}*{b}={c}')
elif a/b == c:
    print(f'{a}/{b}={c}')
elif a == b + c:
    print(f'{a}={b}+{c}')
elif a == b - c:
    print(f'{a}={b}-{c}')
elif a == b*c:
    print(f'{a}={b}*{c}')
else:
    print(f'{a}={b}/{c}')