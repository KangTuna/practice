import sys

input = sys.stdin.readline

N = int(input().rstrip())

data = {}
for _ in range(N):
    k,v = input().rstrip().split()
    data[k] = v
    