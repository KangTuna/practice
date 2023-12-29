import sys

input = sys.stdin.readline

def T(n):
    temp = 0
    for i in range(1,n+1):
        temp += i
    return temp

def W(n):
    temp = 0
    for i in range(1,n+1):
        temp += i*T(i+1)
    return temp

n = int(input().rstrip())
for _ in range(n):
    a = int(input().rstrip())
    print(W(a))
