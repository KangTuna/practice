import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n-1,-1,-1):
    blank = ' ' * i
    print(f'{blank:*>{n}}'.rstrip())

for i in range(1,n):
    blank = ' ' * i
    print(f'{blank:*>{n}}'.rstrip())