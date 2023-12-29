import sys

input = sys.stdin.readline

N = int(input().rstrip())
data = list(map(int,input().rstrip().split()))

data.sort()
print(data[-1]+data[-2])