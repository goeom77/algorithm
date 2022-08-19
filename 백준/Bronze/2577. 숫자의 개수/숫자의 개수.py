x = 1
for t in range(3):
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        x *= arr[i]
result = str(x)
result_arr = [0]*10
for i in result:
    result_arr[int(i)] += 1
for j in range(10):
    print(result_arr[j])