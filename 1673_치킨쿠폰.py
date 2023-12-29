import sys

input= sys.stdin.readline

while True:
    try:
        n,k = map(int,input().rstrip().split())
        ans = 0
        m = n * k
        while True:
            if m//k < 1:
                break
            ans += m//k
            m = (m//k) + (m%k)
        print(ans)
    except:
        break