from collections import Counter
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

ans = int(sys.stdin.readline().rstrip())
cnt = Counter(arr)
try:
    print(cnt[ans])
except:
    print(0)