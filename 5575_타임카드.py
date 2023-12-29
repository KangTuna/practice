import sys

input = sys.stdin.readline

for _ in range(3):
    a,b,c,d,e,f = map(int,input().rstrip().split())
    start = 3600*a + 60*b + c
    end = 3600*d + 60*e + f

    ans = end - start
    hour = ans //3600
    ans %= 3600
    min = ans // 60
    ans %= 60
    sec = ans
    print(hour,min,sec)