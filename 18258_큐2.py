import sys
from collections import deque

deq = deque()
input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    try:
        data = input().rstrip()
        command,x = data.split()
        x = int(x)
    except:
        command = data
    
    if command == "push":
        deq.append(x)
    elif command == "pop":
        try:
            print(deq.popleft())
        except:
            print(-1)
    elif command == "size":
        print(len(deq))
    elif command == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        try:
            print(deq[0])
        except:
            print(-1)
    elif command == "back":
        try:
            print(deq[-1])
        except:
            print(-1)
