import sys

input = sys.stdin.readline
N,M = map(int,input().rstrip().split())

set_data = [input() for _ in range(N)]
check_data = [input() for _ in range(M)]
count = 0
for i in check_data:
    if i in set_data:
        count += 1

print(count)