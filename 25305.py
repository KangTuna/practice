import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
print(arr[-K])
