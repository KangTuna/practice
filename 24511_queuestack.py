import sys

input = sys.stdin.readline

n = int(input().rstrip())

queuestack = list(map(int,input().rstrip().split()))
data = list(map(int,input().rstrip().split()))
m = int(input().rstrip())
prob = list(map(int,input().rstrip().split()))
count = 0
ans = []
for i in range(n-1,-1,-1):
    if queuestack[i] == 0:
        ans.append(data[i])
        count+=1
    if count == m:
        break

for i in ans:
    print(i,end = ' ')
for i in range(m-count):
    print(prob[i],end = ' ')