import sys

N = sys.stdin.readline().rstrip()
arr = []

for i in N:
    arr.append(int(i))

arr.sort(reverse=True)

for i in arr:
    print(i,end="")