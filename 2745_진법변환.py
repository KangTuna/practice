import sys

input = sys.stdin.readline

a,b = input().rstrip().split() # ord(a) - 55
b = int(b)
ans = 0
for i in range(len(a)):
    if ord(a[-(i+1)]) > 64:
        n = ord(a[-(i+1)]) - 55
        ans += (n * (b**i))
    else:
        n = int(a[-(i+1)])
        ans += (n * (b**i))
print(ans)