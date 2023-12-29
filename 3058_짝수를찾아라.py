import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    data = list(map(int,input().rstrip().split()))
    ans = []
    for i in data:
        if i % 2 == 0:
            ans.append(i)
    print(sum(ans),min(ans))