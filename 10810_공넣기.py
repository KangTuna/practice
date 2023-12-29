import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

basket = [0 for _ in range(N+1)]

for _ in range(M):
    i,j,k = map(int,input().rstrip().split())
    for x in range(i,j+1):
        basket[x] = k
    
basket.pop(0)
for i in basket:
    print(i,end = " ")