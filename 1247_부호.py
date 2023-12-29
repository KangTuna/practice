import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input().rstrip())
    temp = 0
    for i in range(n):
        temp += int(input().rstrip())
    if temp > 0:
        print('+')
    elif temp < 0:
        print('-')
    else:
        print('0')
