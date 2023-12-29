import sys

input = sys.stdin.readline

while True:
    ans = 0
    a, b = map(int, input().rstrip().split())
    if a == 0 and b == 0:
        break
    else :
        c = str(a+b)
        for i in range(len(c)):
            if (a%(10**(i+1)))//(10**i)+(b%(10**(i+1)))//(10**i) >= 10:
                ans += 1
                a += 10**(i+1)
        
    print(ans)