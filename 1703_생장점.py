import sys

input = sys.stdin.readline

data = list(map(int,input().rstrip().split()))

while data != [0]:
    n = data.pop(0)
    temp = 1
    for i in range(len(data)):
        if i%2 == 0:
            temp *= data[i]
        else:
            temp -= data[i]
    
    print(temp)
    data = list(map(int,input().rstrip().split()))

