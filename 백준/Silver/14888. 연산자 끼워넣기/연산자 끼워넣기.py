import sys
# 16139 인간 - 컴퓨터 상호작용
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
# plus, minus, multi, devide
d_list = list(map(int, input().split()))

max_value = int(-1e9)
min_value = int(1e9)

def count(S,c_list,idx):
  global min_value
  global max_value
  if idx == N:
    max_value = max(S,max_value)
    min_value = min(S,min_value)
    return
  for i in range(4):
    if c_list[i] > 0:
      c_list[i] -= 1
      # plus
      if i == 0:
        count(S + a[idx],c_list,idx+1)
      # minus
      elif i == 1:
        count(S - a[idx],c_list,idx+1)
      # multi
      elif i == 2:
        
        count(S * a[idx],c_list,idx+1)
      # devide
      elif i == 3:
        count(int(S / a[idx]),c_list,idx+1)
      # back traking
      c_list[i] += 1

count(a[0],d_list,1)
print(max_value)
print(min_value)