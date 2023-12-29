import sys

input = sys.stdin.readline

a,b = map(int,input().rstrip().split())

data = []

for i in range(a):
    temp = []
    tmp = input().rstrip()
    for j in tmp:
        temp.append(int(j))
    data.append(temp)
    

