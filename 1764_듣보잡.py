import sys

input = sys.stdin.readline
N,M = map(int,input().rstrip().split())
listen = []
see = []
for _ in range(N):
    listen.append(input().rstrip())
for _ in range(M):
    see.append(input().rstrip())

see = set(see)
ans = []
count = 0
for i in listen:
    if i in see:
        ans.append(i)
        count += 1
print(count)
ans.sort()
for i in ans:
    print(i)
