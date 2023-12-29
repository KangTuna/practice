import sys

input = sys.stdin.readline

N = int(input().rstrip())
data = list(map(int,input().rstrip().split()))
data.sort()

print(data[0]*data[-1])