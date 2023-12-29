import sys

input = sys.stdin.readline

a,b,c,d = input().rstrip().split()

front = f'{a}{b}'
back = f'{c}{d}'

print(int(front) + int(back))