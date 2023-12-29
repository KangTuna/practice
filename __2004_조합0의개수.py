import sys
import time
input = sys.stdin.readline

def com(n,r):
    temp = 1
    for i in range(n,r-1,-1):
        temp *= i
    div = 1
    for i in range(r,0,-1):
        div *= i
    return int(temp/div)

n,r = map(int,input().rstrip().split())
now = time.time()
print(now)
data = str(com(n,r))
count = 0
print(time.time() - now)
for i in range(len(data)-1,-1,-1):
    if data[i] == "0":
        count += 1
    else:
        break
print(time.time() - now)

print(count)