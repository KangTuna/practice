import sys

N = int(sys.stdin.readline().rstrip())

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

print(fibo(N))
