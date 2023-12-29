import sys

input = sys.stdin.readline

def facto(n):
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans

def bc(n,k):
    return facto(n) // facto(k) // facto(n-k)

N,K = map(int,input().rstrip().split())

print(bc(N,K)%1_000_000_007)