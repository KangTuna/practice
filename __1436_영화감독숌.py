import sys

input = sys.stdin.readline

N = int(input().rstrip())

data = [str(x) for x in range(1,10001)]
count = 0
ans = ''
i = 0
while True:
    i = int(i)
    i += 1
    i = str(i)
    if '666' in i:
        count += 1
    if count == N:
        print(i)
        break
