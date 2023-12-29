import sys

input = sys.stdin.readline

data = []
for _ in range(5):
    data.append(input().rstrip())

ans = []
for i in data:
    if 'FBI' in i:
        ans.append(data.index(i)+1)

if len(ans) == 0:
    print('HE GOT AWAY!')
else:
    for i in ans:
        print(i,end = ' ')