import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n-1,-1,-1):
    temp = ' ' * (2*i)
    print(f'{temp:*^{2*n}}')

for i in range(1,n):
    temp = ' ' * (2*i)
    print(f'{temp:*^{2*n}}')