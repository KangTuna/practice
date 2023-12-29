import sys

input = sys.stdin.readline

N = int(input().rstrip())

max_area = [-100000,-100000]
min_area = [100000,100000]
for _ in range(N):
    x,y = map(int,input().rstrip().split())
    if x >= max_area[0]:
        max_area[0] = x
    if y >= max_area[1]:
        max_area[1] = y
    if x <= min_area[0]:
        min_area[0] = x
    if y <= min_area[1]:
        min_area[1] = y
    
print((max_area[0]-min_area[0]) * (max_area[1]-min_area[1]))
