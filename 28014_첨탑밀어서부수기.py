import sys

input = sys.stdin.readline

t = int(input().rstrip())
data = list(map(int,input().rstrip().split()))
tower = 0
count = 0
for _ in range(len(data)):
  target = data.pop(0)
  if tower > target:
    continue
  else:
    tower = target
    count += 1

print(count)
  