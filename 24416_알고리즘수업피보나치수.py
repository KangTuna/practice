import sys

input = sys.stdin.readline

def fibonacci(n):
    
    f = [1 for _ in range(n+1)]
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

N = int(input().rstrip())

print(fibonacci(N),N-2)

