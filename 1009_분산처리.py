import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    a,b = map(int,input().rstrip().split())
    b %= 10
    print((a**b)%10)