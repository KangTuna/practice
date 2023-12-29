import sys

input = sys.stdin.readline

a,b = map(int,input().rstrip().split())

while a+b != 0:
    if a>b:
        print('Yes')
    else:
        print('No')
    a,b = map(int,input().rstrip().split())