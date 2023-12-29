import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

ans = []
N,K = map(int,input().rstrip().split())
for i in range(1,N+1):
    deq.append(i)

while len(deq) != 0:
    deq.rotate(-K)
    ans.append(deq.pop())

print(f"<{ans[0]}",end="")
for i in range(1,len(ans)):
    print(f", {ans[i]}",end="")
print(">")

