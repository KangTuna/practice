import sys,math

input = sys.stdin.readline

n = int(input().rstrip())
count = 0
# for i in range(n,0,-1):
#     if math.gcd(n,i) == 1:
#         count += 1
m = int(math.sqrt(n)) + 1
for i in range(m):
    if math.gcd(n,i) != 1:
        count += 1
print(count)