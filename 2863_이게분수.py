import sys

input = sys.stdin.readline

a,b = map(int,input().rstrip().split())
c,d = map(int,input().rstrip().split())

data = [[a,b],
        [c,d]]

def turn(n):
    temp = n
    temp[0][0],temp[0][1],temp[1][0],temp[1][1] = temp[1][0],temp[0][0],temp[1][1],temp[0][1]
    return temp

def result(n):
    return (n[0][0]/n[1][0]) + (n[0][1]/n[1][1])

max = 0
ans = 0
for i in range(4):
    a = result(data)
    if max < a:
        ans = i
        max = a
    data = turn(data)

print(ans)