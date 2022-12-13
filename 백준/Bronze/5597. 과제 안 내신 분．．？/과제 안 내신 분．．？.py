arr = [0]*30
for i in range(28):
    a = int(input())
    arr[a-1] = 1
for i in range(30):
    if arr[i] == 0:
        print(i+1)