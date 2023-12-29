import sys

input = sys.stdin.readline

N = int(input().rstrip())
ans = []
for _ in range(N):
    string = input().rstrip().lower()
    ans.append(string)

for i in ans:
    print(i)