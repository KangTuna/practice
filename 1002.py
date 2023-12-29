import math

T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    minus = math.sqrt((r2-r1)**2)
    plus = r1+r2
    r3 = ((x2-x1) + (y2-y1))**2
    r3 = math.sqrt(r3)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if minus == r3 or plus == r3:
            print(1)
        elif minus > r3 or plus < r3:
            print(0)
        elif minus < r3 or plus > r3:
            print(2)
        elif r3 == r1 or r3 == r2:
            print(2)

