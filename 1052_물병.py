import sys,math

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
pre = n
start = int(math.log2(n)) + 1
data = []
while n > 0:
    if n >= 2**start:
        data.append(2**start)
        n -= 2**start
    else:
        start -= 1
    if n == 0:
        break
print(data)
print(sum(data) - pre)
