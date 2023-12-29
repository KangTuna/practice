import sys

input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
data = []
for i in range(N):
    data.append(input().rstrip())
ans = []
for i in range(M):
    a = input().rstrip()
    try:
        a = int(a)
        ans.append(a)
    except:
        ans.append(a)
for i in ans:
    if type(i) == int:
        print(data[i-1])
    else:
        print(data.index(i)+1)