# 색종이 만들기
from collections import deque
n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
white_paper = 0
blue_paper = 0
q = deque([(0,0)])
def paper_size(x,y,size):
    global white_paper
    global blue_paper
    cnt = field[y][x]
    if size==1:
        if cnt:
            blue_paper += 1
        else:
            white_paper += 1
    else:        
        onepaper = True
        for j in range(size):
            for i in range(size):
                if field[y+j][x+i] != cnt:
                    onepaper = False
                    break
            if not onepaper:
                break
        if onepaper:
            if cnt:
                blue_paper += 1
            else:
                white_paper += 1
        else:
            size //= 2
            paper_size(x,y,size)
            paper_size(x+size,y,size)
            paper_size(x,y+size,size)
            paper_size(x+size,y+size,size)
paper_size(0,0,n)
print(white_paper)
print(blue_paper)

