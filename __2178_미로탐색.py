import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
data = []
for _ in range(N):
    idx = input().rstrip()
    tmp = []
    for i in idx:
        tmp.append(int(i))
    data.append(tmp)

for i in data:
    i.append(0)
data.append([0 for _ in range(M)])
visited = [list(map(bool,x)) for x in data]
start = [0,0]
end = (M-1,N-1)
index = start
count = 0
while index != end:
    visited[index[0]][index[1]] = False
    if data[index[0]+1][index[1]] == 1 and visited[index[0]+1][index[1]] == True:
        index[0] += 1
        count += 1
    if data[index[0]][index[1]+1] == 1 and visited[index[0]][index[1]+1] == True:
        index[1] += 1
        count += 1
    if data[index[0]-1][index[1]] == 1 and visited[index[0]-1][index[1]] == True:
        index[0] -= 1
        count += 1
    if data[index[0]][index[1]-1] == 1 and visited[index[0]][index[1]-1] == True:
        index[1] -= 1
        count += 1
    print(count)

print(count)