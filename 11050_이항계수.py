import sys

input = sys.stdin.readline

def bc(n,k):
    if n == 0 or k == 0 or n == k:
        return 1
    else:
        return bc(n-1,k-1) + bc(n-1,k)

x,y = map(int,input().rstrip().split())
print(bc(x,y))