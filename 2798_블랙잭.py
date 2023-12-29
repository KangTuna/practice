import sys

input = sys.stdin.readline

N,target = map(int,input().rstrip().split())

data = list(map(int,input().rstrip().split()))
max = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            temp = data[i]+data[j]+data[k]
            if temp > target:
                continue
            elif temp == target:
                max = temp
                break
            elif temp > max:
                max = temp

print(max)