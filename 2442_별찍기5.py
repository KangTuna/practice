import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    star = '*' *(2*i + 1)
    print(f'{star:^{2*n-1}}'.rstrip())