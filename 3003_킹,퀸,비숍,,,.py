import sys

input = sys.stdin.readline

data = list(map(int,input().rstrip().split()))

ans = [1,1,2,2,2,8]

for i in range(len(data)):
    print(ans[i] - data[i],end=" ")