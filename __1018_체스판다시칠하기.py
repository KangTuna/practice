import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

data = [list(map(str,input().rstrip())) for _ in range(N)]

min_count = 8*8
max_count = 0
error_a = []
ans = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]


for i in range(N-7):
    for j in range(M-7):
        error = 0
        for k in range(8):
            for v in range(8):
                if ans[k][v] != data[i+k][j+v]:
                    error += 1
        error_a.append(error)

min_count = min(error_a)
max_count = max(error_a)
if min_count < 64-max_count:
    print(min_count)
else:
    print(64-max_count)

