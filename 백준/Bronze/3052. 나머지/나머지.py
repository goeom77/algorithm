arr = []
for i in range(10):
    arr.append(int(input())%42)
brr = set(arr)
arr = list(brr)
print(len(arr))