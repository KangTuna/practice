import sys

N = int(sys.stdin.readline().rstrip())
last = 0
if N == 1:
    last = 1
else:
    check = [2**x for x in range(20)]
    for i in check:
        if i/2 < N <= i:
            N -= int(i/2)
            break
    if N == 0:
        last = 2
    else:
        for i in range(N):
            last += 2
print(last)