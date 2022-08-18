import math
a,b = map(int,input().split())
# 최대 공약수 
print(math.gcd(a,b))
# 최소 공배수
print(math.lcm(a,b))