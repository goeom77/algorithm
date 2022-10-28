import sys
sys.setrecursionlimit(10 ** 6)
temp = sys.stdin.readline

tree = []

def post_order(start, end):
    if start > end:
        return
    
    root = tree[start]
    idx = start + 1
    
    while idx <= end:
        if root < tree[idx]: # 가장 작을 때까지 들어가기
            break
        idx += 1
    # 후위 순회
    post_order(start+1, idx-1) # 마지막 값들
    post_order(idx, end) # 제일 작은 값들
    print(root)
    

while True:
    try:
        tree.append(int(input()))
    except:
        break

post_order(0, len(tree)-1)

