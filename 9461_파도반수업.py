import sys

input = sys.stdin.readline

def wave(n):
    f = [1 for _ in range(n+1)]
    for i in range(4,n+1):
        f[i] = f[i-2]+f[i-3]
    return f[n]

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    print(wave(N))