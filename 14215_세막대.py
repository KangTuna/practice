import sys

input = sys.stdin.readline

data = list(map(int,input().rstrip().split()))
data.sort()
hypo = data.pop()
a,b = data[0],data[1]

while True:
    if hypo < (a+b):
        break
    else:
        hypo -= 1

print(hypo+a+b)
