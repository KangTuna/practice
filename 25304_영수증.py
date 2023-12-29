import sys

price = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
bill = 0
for _ in range(N):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    bill += a*b

if price == bill:
    print('Yes')
else:
    print('No')