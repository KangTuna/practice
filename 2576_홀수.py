import sys

input = sys.stdin.readline

data = []

for _ in range(7):
    number = int(input().rstrip())
    if number % 2 == 1:
        data.append(number)

if len(data) > 0:
    print(sum(data))
    print(min(data))
else:
    print(-1)