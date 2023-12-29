import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

arr.sort()
for i in arr:
    print(i[0],i[1])
