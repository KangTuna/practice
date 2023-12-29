import sys

input = sys.stdin.readline

x,y = map(int,input().rstrip().split())

def gcd(a,b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a
a = gcd(x,y) 
print(a)
b = int((x*y)/a)
print(b)
