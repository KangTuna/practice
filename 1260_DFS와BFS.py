from collections import deque
import sys

input= sys.stdin.readline

N,M,V = map(int,input().rstrip().split())
graph = {x:list() for x in range(N+1)}
for _ in range(M):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph.values():
    i.sort()

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start,visited):
    queue = deque([start])
    visited.append(start)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return visited

visited_dfs = list()
visited_bfs = list()
ans1 = dfs(graph,V,visited_dfs)
ans2 = bfs(graph,V,visited_bfs)
for i in ans1:
    print(i,end = ' ')
print()
for j in ans2:
    print(j,end = ' ')