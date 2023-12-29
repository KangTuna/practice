import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

basket = [x for x in range(N+1)]

for _ in range(M):
    i,j,k = map(int,input().rstrip().split())
    for x in range(j-k+1):
        basket.insert(i,basket.pop(j))
basket.pop(0)
for i in basket:
    print(i,end = " ")
