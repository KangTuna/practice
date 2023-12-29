import sys

input = sys.stdin.readline

N = int(input().rstrip())

data = [2 for _ in range(11)]
count = 0
for _ in range(N):
    num,place = map(int,input().rstrip().split())
    if data[num] != 2 and data[num] != place:
        data[num] = place
        count += 1
    elif data[num] == 2:
        data[num] = place

print(count) 
