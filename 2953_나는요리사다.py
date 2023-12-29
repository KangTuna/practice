import sys

input = sys.stdin.readline

data = []

for _ in range(5):
    data.append(sum(list(map(int,input().rstrip().split()))))

winner = data.index(max(data)) + 1
ans = max(data)

print(winner, ans)