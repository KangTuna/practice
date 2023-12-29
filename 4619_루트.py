import sys

input = sys.stdin.readline

while True:
    b,n = map(int,input().rstrip().split())
    if b == 0 and n == 0:
        break
    for a in range(1,1000001):
        if a**n == b:
            ans = a
            break
        elif a**n > b:
            if abs(((a-1) ** n) - b) > abs((a ** n) - b):
                ans = a
            else:
                ans = a-1
            break
            
    print(ans)