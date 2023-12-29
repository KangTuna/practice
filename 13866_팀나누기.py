import sys

input = sys.stdin.readline

data = list(map(int,input().rstrip().split()))

max1 = data.pop(data.index(max(data)))
min1 = data.pop(data.index(min(data)))

print(abs(sum(data) - (max1 + min1)))