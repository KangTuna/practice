import sys

input = sys.stdin.readline

n = int(input().rstrip())

data = list(map(int,input().rstrip().split()))
count = 1
ans = 0
for i in data:
    if i == 1:
        ans += i*count
        count += 1
    else:
        count = 1

print(ans)