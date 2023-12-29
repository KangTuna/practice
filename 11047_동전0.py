import sys

input = sys.stdin.readline

N,K = map(int,input().rstrip().split())
coin = []
for _ in range(N):
    coin.append(int(input().rstrip()))
coin.reverse()
count = 0
for i in coin:
    count += K//i
    K %= i
print(count)