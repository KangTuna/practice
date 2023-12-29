import sys

input = sys.stdin.readline

a,n = map(int,input().rstrip().split())

print(a*(n-1)+1) 