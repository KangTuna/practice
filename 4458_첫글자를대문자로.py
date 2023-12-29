import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    ans = input().rstrip()
    a = ans[0]
    b = a.upper()
    ans = ans.replace(a,b,1)
    print(ans)