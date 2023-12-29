import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

data = list(map(int,input().rstrip().split()))

people = n*m
for i in data:
    print(i - people,end = " ")