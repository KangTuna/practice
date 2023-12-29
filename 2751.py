import sys

arr = [0 for i in range(10001)]

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    arr[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)