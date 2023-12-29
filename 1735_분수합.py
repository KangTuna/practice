import sys

input = sys.stdin.readline

def gcd(n,m):
    r = 0
    while True:
        if n%m == 0:
            return m
        else:
            r = n%m
            n = m
            m = r

A1,B1 = map(int,input().rstrip().split())
A2,B2 = map(int,input().rstrip().split())
A3,B3 = (A1*B2)+(B1*A2),B1*B2
g = gcd(A3,B3)
A3,B3 = A3//g,B3//g

print(A3,B3)