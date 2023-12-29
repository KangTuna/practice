import sys
from functools import cache
sys.setrecursionlimit(10000)
input = sys.stdin.readline
@cache
def facto(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*facto(n-1)

N = int(input().rstrip())
ans = str(facto(N))
count = 0
for i in range(len(ans)-1,-1,-1):
    if ans[i] == '0':
        count+=1
    else:
        break
print(count)
