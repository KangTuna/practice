import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
def is_palindrome(n):
    m = str(n)
    for i in range(len(m)):
        if m[i] != m[-(i+1)]:
            return False
    return True
N = int(input().rstrip())
while True:
    if is_prime(N) and is_palindrome(N):
        break
    else:
        N += 1

print(N)
