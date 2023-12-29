import sys
from collections import deque

deq = deque()
input = sys.stdin.readline
def dfs(R):
    global visited
    visited[R] = True
    deq.append(R)
    for i in data:
        if i[0] == R:
            if visited[i[1]] != True:
                dfs(i[1])
            else:
                return
N,M,R = map(int,input().rstrip().split())
visited = [False for _ in range(N+1)]
data = [list(map(int,input().rstrip().split())) for _ in range(N)]
data.sort()
dfs(R)
for i in range(1,len(visited)):
    if visited[i] == False:
        deq.insert(i,0)

for i in deq:
    print(i)