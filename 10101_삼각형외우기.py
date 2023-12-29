import sys

input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())

data = [a,b,c]

if sum(data) == 180:
    temp = data.pop()
    if data.count(temp) == 2:
        print('Equilateral')
    elif data.count(temp) == 1:
        print('Isosceles')
    elif data[0] == data[-1]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')