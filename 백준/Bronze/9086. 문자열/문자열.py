n = int(input())
for i in range(n):
    arr = list(input())
    sentence = arr[0]+arr[-1]
    print(''.join(sentence))