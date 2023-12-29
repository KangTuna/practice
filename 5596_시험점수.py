import sys

input = sys.stdin.readline

data1 = list(map(int,input().rstrip().split()))
data2 = list(map(int,input().rstrip().split()))

print(max(sum(data1),sum(data2)))
    