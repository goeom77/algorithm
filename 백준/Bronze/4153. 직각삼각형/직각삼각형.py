a,b,c = map(int,input().split())
while (a,b,c) !=(0,0,0):
    if (c**2) == (a**2) + (b**2):
        print('right')
    elif (c**2) + (a**2) == (b**2):
        print('right')
    elif (c**2) + (b**2) == (a**2):
        print('right')
    else:
        print('wrong')
    a,b,c = map(int,input().split())