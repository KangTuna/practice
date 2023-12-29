import sys

input = sys.stdin.readline

N = int(input().rstrip())

data = [input().rstrip() for _ in range(N)]
enter = []
count = 0

if data.count('ENTER') == 1:
    data = list(set(data))
    print(len(data) - 1)
else:
    data.pop(0)
    while len(data) > 0:
        enter = []
        while len(data) > 0:
            temp = data.pop(0)
            if temp == 'ENTER':
                break
            else:
                enter.append(temp)
        enter = list(set(enter))
        count += len(enter)
    print(count)

    