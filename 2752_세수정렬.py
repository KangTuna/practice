import sys

input = sys.stdin.readline

data = list(map(int,input().rstrip().split()))

first = data.pop(data.index(min(data)))
last = data.pop(data.index(max(data)))
middle = data[0]

print(first,middle,last)