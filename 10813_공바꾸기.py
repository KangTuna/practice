import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

basket = [x for x in range(N+1)]

for _ in range(M):
    i,j = map(int,input().rstrip().split())
    basket[i],basket[j] = basket[j],basket[i]

basket.pop(0)

for i in basket:
    print(i,end = " ")
    