import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    arr.append(num)

arr.sort()
for i in arr:
    print(i)