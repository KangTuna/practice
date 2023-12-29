import sys

input = sys.stdin.readline

def facto(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def combi(n,r):
    return (facto(n)//(facto(r)*facto(n-r)))

n = int(input().rstrip())

temp = 0
if n%2 == 0:
    for i in range((n//2)+1):
        temp += combi(n-i,i)
else:
    for i in range((n//2)+1):
        temp += combi(n-i,n-(i*2))
print(temp%10007)



    
