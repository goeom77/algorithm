x = int(input())
y = [64,32,16,8,4,2,1]
count = 0
for i in y:
    if x >=i:
        x -= i
        count +=1
print(count)