import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())

white = [[False for _ in range(100)]for _ in range(100)]
for _ in range(N):
    y,x = map(int,sys.stdin.readline().rstrip().split())
    for i in range(10):
        for j in range(10):
            white[x+i][y+j] = True
ans = []
for i in range(100):
    ans += white[i]
print(Counter(ans)[True])

