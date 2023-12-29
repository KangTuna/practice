from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
N = int(input())
for i in range(N):
    n = int(input())
    if n == 0:
        print(1,0)
    else:
        print(fibo(n-1),fibo(n))