import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n,0,-1):
    star = '*' * (2*i-1)
    print(f'{star:^{2*n-1}}'.rstrip())

for i in range(2,n+1):
    star = '*' * (2*i-1)
    print(f'{star:^{2*n-1}}'.rstrip())
