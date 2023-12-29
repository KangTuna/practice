import sys

input = sys.stdin.readline

price,count,money = map(int,input().rstrip().split())

if money >= price*count:
    print(0)
else:
    print((price*count)-money)
