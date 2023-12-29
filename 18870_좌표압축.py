import sys

N = int(sys.stdin.readline().rstrip())

data = list(map(int,sys.stdin.readline().rstrip().split()))
pre = data
data = list(set(data))
data.sort()
dic = {}
for i in range(len(data)):
    dic[data[i]] = i

ans = []
for i in range(len(pre)):
    ans.append(dic[pre[i]])

for i in ans:
    print(i,end=" ")