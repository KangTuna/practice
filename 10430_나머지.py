import sys

input = sys.stdin.readline

A,B,C = map(int,input().rstrip().split())

a = (A+B)%C
b = ((A%C) + (B%C))%C
c = (A*B)%C
d = ((A%C) * (B%C))%C

print(a)
print(b)
print(c)
print(d)

