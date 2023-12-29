import sys

input = sys.stdin.readline

x,y = map(int,input().rstrip().split())
while not (x ==0 and y == 0):
    if x % y == 0 and x//y > 0:
        print("multiple")
    elif y % x == 0 and y//x > 0:
        print("factor")
    else:
        print("neither")
    x,y = map(int,input().rstrip().split())
