import sys

input = sys.stdin.readline

# N,r,c = map(int,input().rstrip().split())

N = 3

data = [[]]
x_ = 0
for i in range(2**N):
    if i % 2 == 0:
        data[0].append(x_)
        x_ += 1
    else:
        data[0].append(x_)
        x_ += 3

print(data)