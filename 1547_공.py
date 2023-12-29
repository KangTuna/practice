import sys

input = sys.stdin.readline

n = int(input().rstrip())

ball = [0,1,0,0]
for _ in range(n):
    a,b = map(int,input().rstrip().split())
    ball[a],ball[b] = ball[b],ball[a]

print(ball.index(1))