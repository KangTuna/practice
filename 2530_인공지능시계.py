import sys

input = sys.stdin.readline

H,M,S = map(int,input().rstrip().split())
T = int(input().rstrip())

T += (H*3600) + (M*60) + S
H,M,S = 0,0,0

H += T//3600
T %= 3600
M += T//60
T %= 60
S += T
H %= 24
print(H,M,S)