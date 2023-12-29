import sys

N = int(sys.stdin.readline().rstrip())
data = set(map(int,sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
check = list(map(int,sys.stdin.readline().rstrip().split()))
ans = []

for i in check:
    if i in data:
        ans.append(1)
    else:
        ans.append(0)

for i in ans:
    print(i,end=" ")