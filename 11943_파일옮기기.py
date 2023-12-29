import sys

input = sys.stdin.readline

a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))

print(min(a[0] + b[1],a[1] + b[0]))