a,b,c,d,e = map(int, input().split())
a %= 10
b %= 10
c %= 10
d %= 10
e %= 10

a = (a*a)%10
b = (b*b)%10
c = (c*c)%10
d = (d*d)%10
e = (e*e)%10
result = a+b+c+d+e
print(result%10)