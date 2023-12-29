import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    data = list(map(int,sys.stdin.readline().rstrip().split()))
    data[0],data[1] = data[1],data[0]
    arr.append(data)

arr.sort()
for i in arr:
    print(i[1],i[0])