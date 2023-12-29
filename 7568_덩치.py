import sys

input = sys.stdin.readline

N = int(input().rstrip())
data = []
for _ in range(N):
    weight,height = map(int,input().rstrip().split())
    data.append((weight,height))
ans  = []

for i in range(N):
    count = 1
    for j in range(N):
        if i == j:
            continue
        else:
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                count += 1
    ans.append(count)

for i in ans:
    print(i,end=" ")