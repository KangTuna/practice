import sys
N = sys.stdin.readline().rstrip()
A = set(map(int,sys.stdin.readline().rstrip().split()))
M = sys.stdin.readline().rstrip()
B = list(map(int,sys.stdin.readline().rstrip().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)
