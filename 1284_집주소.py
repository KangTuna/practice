import sys

input = sys.stdin.readline

data = input().rstrip()
while data != '0':
    length = 0
    for i in data:
        if i == '0':
            length += 4
        elif i == '1':
            length += 2
        else:
            length += 3
    length += len(data) + 1
    print(length)
    data = input().rstrip()
