import sys
input = sys.stdin.readline
# 1662 압축

# 숫자(글자) = 글자를 숫자만큼 반복 , 숫자는 1글자 총 글자수는?
# "("가 처음에 나오는 것은 상관없지만 ")"가 나오고 나서 "("가 나오면 갱신을 해줘야 한다.
# 그럼 들고있는 값들을 list로 보관해서 cnt를 통해 관리를 하면된다. cnt는 글자의 개수, before는 압축횟수, 
input_data = input().strip()

def solv():
    stack = []
    cnt=0
    before=''
    for c in input_data:
        if c == '(':
            stack.append([cnt-1,before])
            cnt = 0
        elif c == ')':
            info = stack.pop()
            cnt = cnt*info[1]+info[0]
        else:
            cnt += 1
            before = int(c)
    print(cnt)
solv()