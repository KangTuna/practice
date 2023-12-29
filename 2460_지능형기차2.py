import sys

input = sys.stdin.readline
M = 0
person = 0
for _ in range(10):
    o,i = map(int,input().rstrip().split())
    person -= o
    person += i
    if person > M:
        M = person

print(M)