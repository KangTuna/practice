import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
friend = [set() for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    friend[a-1].add(b)
    friend[b-1].add(a)

for i in friend:
    print(len(i))