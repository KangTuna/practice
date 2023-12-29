import sys

input = sys.stdin.readline

N = int(input().rstrip())
star = "*"

count = [x for x in range(1,N*2,2)]
for i in range(N*2-3,0,-2):
    count.append(i)

for i in range(N*2-1):
    print(f"{star*count[i]:^{N*2-1}}".rstrip())