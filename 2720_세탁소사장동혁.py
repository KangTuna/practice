import sys

input = sys.stdin.readline

n = int(input().rstrip())
size = [25,10,5,1]
ans = []
for _ in range(n):
    c = int(input().rstrip())
    data = []
    for i in size:
        data.append(c//i)
        c %= i
    ans.append(data)

for i in ans:
    for j in i:
        print(j,end = " ")
    print()

