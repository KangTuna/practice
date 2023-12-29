import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

A = set(map(int,input().rstrip().split()))
B = set(map(int,input().rstrip().split()))
ans = len(A-B) + len(B-A)

print(ans)