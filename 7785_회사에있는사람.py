import sys

input = sys.stdin.readline

n = int(input().rstrip())
data = []
for i in range(n):
    n,t = input().rstrip().split()
    if t == 'enter':
        data.append(n)
    else:
        data.remove(n)

data.sort(reverse= True)
for i in data:
    print(i)