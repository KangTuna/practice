import sys

input = sys.stdin.readline

n = int(input().rstrip())

data = [[0 for _ in range(n)]]
visited = [False for _ in range(n+1)]
for _ in range(n):
    data.append(list(map(int,input().rstrip().split())))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]




            