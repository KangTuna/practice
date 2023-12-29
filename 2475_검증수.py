import sys

input = sys.stdin.readline

N = map(int,input().rstrip().split())
temp = 0
for i in N:
    temp += i*i

print(temp%10)