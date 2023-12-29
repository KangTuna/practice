import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    data = input().rstrip()
    print(f"{data[0]}{data[-1]}")