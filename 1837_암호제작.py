import sys

input = sys.stdin.readline

pq,k = map(int,input().rstrip().split())
ans = 1
for i in range(2,k):
    if pq % i == 0:
        print(f'BAD {i}')
        ans = 0
        break

if ans == 1:
    print('GOOD')