import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ans = []

def dfs():
    if len(ans) == M:
        print(' '.join(map(str,ans)))
        return
    else:
        for i in range(1,N+1):
            for j in range(i,N+1): 
                if i not in ans:
                    ans.append(i) 
                    dfs()
                    ans.pop()
            
dfs()