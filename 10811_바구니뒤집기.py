import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

basket = [x for x in range(N+1)]
for _ in range(M):
    i,j = map(int,input().rstrip().split())
    for k in range(int((j-i)/2)+1):
        basket[i+k],basket[j-k] = basket[j-k],basket[i+k]

basket.pop(0)

for i in basket:
    print(i,end=" ")





