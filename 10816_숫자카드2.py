import sys
from collections import Counter
input = sys.stdin.readline

N = int(input().rstrip())
data = list(map(int,input().rstrip().split()))
M = int(input().rstrip())
ans = list(map(int,input().rstrip().split()))
common = Counter(data)
for i in ans:
    print(common[i],end=" ")

