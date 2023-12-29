import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

data = []
ans = 0
for _ in range(n):
    a = []
    for i in input().rstrip():
        a.append(int(i))
    data.append(a)

for i in range(n):
    for j in range(m):
        temp = data[i][j]
        count = 1
        k = 1
        while True:
            if i+k >= n or j+k >= m:
                break
            if temp == data[i+k][j] and temp == data[i][j+k] and temp == data[i+k][j+k]:
                count = k+1
                k += 1
            else:
                k += 1
        ans = max(ans,count)

print(ans**2)