memo = [0 for _ in range(1000)]
memo[1],memo[2] = 1,1
def fibo(n):
    if n < 2 or memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
    
print(fibo(50) + fibo(50))
print(fibo(31) + fibo(55))
print(fibo(100) + fibo(100))