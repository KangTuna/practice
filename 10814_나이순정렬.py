import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    age,name = sys.stdin.readline().rstrip().split()
    data = [int(age),i,name]
    arr.append(data)
arr.sort()
for i in arr:
    print(i[0],i[2])

