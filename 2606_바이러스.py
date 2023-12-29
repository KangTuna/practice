import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

def dfs(g,root):
    visited[root] = True
    for i in g[root]:
        if visited[i] == False:
            dfs(g,i)

for _ in range(M):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 그래프라 반대 간선도 추가

dfs(graph,1)

ans = visited.count(True) -1 # 1은 제외

print(ans)
