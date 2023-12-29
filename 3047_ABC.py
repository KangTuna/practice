import sys

input = sys.stdin.readline

data = list(map(int,input().rstrip().split()))
ans = input().rstrip()
data.sort()
dict1 = {'A' : data[0],'B' : data[1], 'C' : data[2]}

for i in ans:
    print(dict1[i], end = ' ')

