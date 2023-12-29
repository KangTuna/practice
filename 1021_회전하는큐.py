import sys
from collections import deque

dq = deque()

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

data = list(map(int,input().rstrip().split()))

count = 0

for i in range(1,n+1):
    dq.append(i)

def counting(target):
    global dq,count
    while True:
        if dq[0] == target:
            dq.popleft()
            return
        else:
            goal = dq.index(target)
            if goal > (len(dq)//2):
                dq.rotate()
                count += 1

            else:
                dq.rotate(-1)
                count += 1

for i in data:
    counting(i)

print(count)
