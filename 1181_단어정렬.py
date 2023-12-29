import sys

N = int(sys.stdin.readline().rstrip())
arr = [[] for _ in range(51)]
for i in range(N):
    word = sys.stdin.readline().rstrip()
    arr[len(word)].append(word)

for i in range(len(arr)):
    arr[i] = list(set(arr[i]))
    arr[i].sort()
    
for i in arr:
    for j in i:
        print(j)


