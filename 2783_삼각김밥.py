import sys

input = sys.stdin.readline

a,b = map(int,input().rstrip().split())

n = int(input().rstrip())
std = a/b
for _ in range(n):
    c,d = map(int,input().rstrip().split())
    bal = c/d
    std = min(bal,std)

ans = round(std*1000,2)
print(ans)