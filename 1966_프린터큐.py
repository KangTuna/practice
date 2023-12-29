import sys
from collections import deque

deq = deque()
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    deq.clear()
    N,M = map(int,input().rstrip().split())
    important = list(map(int,input().rstrip().split()))
    for i,j in zip(range(N),important):
        deq.append((i,j))
    goal = deq[M][0]
    std = max(important)
    count = 1
    while True:
        if deq[0][0] == goal and deq[0][1] == max(important):
            break
        else:
            if deq[0][1] == std:
                deq.popleft()
                count += 1
                important.pop(important.index(std))
                while std not in important:
                    std -= 1
            else:
                deq.rotate()
    print(count)
    
                

    