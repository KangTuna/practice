import sys

input = sys.stdin.readline

while True:
    data = input().rstrip()
    if data == 'END':
        break
    else:
        for i in range(1,len(data)+1):
            print(data[-i],end = '')
        print()