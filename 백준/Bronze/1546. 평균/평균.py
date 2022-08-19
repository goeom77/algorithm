T = int(input())
arr = list(map(int,input().split()))
num = sum(arr) / (T * max(arr)) *100
print(num)
