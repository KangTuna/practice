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

def lcm(n,m):
    return (n*m)//gcd(n,m)

n,m = map(int,input().rstrip().split())

print(lcm(n,m))
