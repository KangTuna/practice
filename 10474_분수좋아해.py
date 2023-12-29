import sys

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    a,b = map(int,input().rstrip().split())
    ans = (-a) + b + 2
    print(ans)