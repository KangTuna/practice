import sys

input = sys.stdin.readline

n = int(input().rstrip())

i = 1
ans = 0
while i**2 <= n:
    ans += 1
    i += 1

print(ans)