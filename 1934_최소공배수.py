import sys

input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

N = int(input().rstrip())
for _ in range(N):
    x,y = map(int,input().rstrip().split())
    a = gcd(x,y)
    b = int((x*y)/a)
    print(b)
