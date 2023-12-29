import sys
import pprint

pp = pprint.PrettyPrinter(width=41, compact=True)

N = int(sys.stdin.readline().rstrip())

data = []
max = 0
row,col = 0,0
home = [0,0]
while True:
    point,length = map(int,sys.stdin.readline().rstrip().split())
    data.append([point,length])
    if length > max:
        max = length

    if point == 1 or point == 2:
        if row < length:
            row = length

    if length == 1:
        home[0] += length
    elif length == 2:
        home[0] -= length
    elif length == 3:
        home[1] -= length
    elif length == 4:
        home[1] += length
    
    if home[0] == 0 and home[1] == 0:
        break







#1: 동 2: 서 3: 남 4: 북

data = [] 
    