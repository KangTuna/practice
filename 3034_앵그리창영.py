import sys

input = sys.stdin.readline

t,a,b = map(int,input().rstrip().split())

def c(a,b):
    return ((a**2)+(b**2))**(1/2)
for _ in range(t):
    test = int(input().rstrip())
    if test <= c(a,b):
        print('DA')
    else:
        print('NE')
