import sys

input = sys.stdin.readline

string = input().rstrip()
ans = 0
for i in range(len(string)):
    if string[i] == string[-(i+1)]:
        ans = 1
    else:
        ans = 0
        break

print(ans)

