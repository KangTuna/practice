import sys

input = sys.stdin.readline

N = int(input().rstrip())
ans = 0
end = 4*(10**9)
for _ in range(N):
    n = int(input().rstrip())
    for i in range(n,end+1):
        c = 0
        for j in range(2,i):
            if i%j == 0:
                c = 1
                break
        if c == 0:
            ans = i
            break

    print(ans)