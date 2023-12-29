import sys

input = sys.stdin.readline

n = int(input().rstrip())
temp = 0
for _ in range(n):
    temp += int(input().rstrip())

print(temp - n + 1)