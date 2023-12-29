import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

data = list(map(int,input().rstrip().split()))
sum1 = 0
arr = [0]
for i in range(N):
    sum1 += data[i]
    arr.append(sum1)

for i in range(M):
    x,y = map(int,input().rstrip().split())
    print(arr[y] - arr[x-1])
