import sys

input = sys.stdin.readline

N = int(input().rstrip())

count = N // 4
a = "long "
print(f"{a*count}int")
