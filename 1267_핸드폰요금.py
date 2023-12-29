import sys

input = sys.stdin.readline

n = int(input().rstrip())

# Y = 30 : 10
# M = 60 : 15

data = list(map(int,input().rstrip().split()))
young = 0
min = 0
for i in data:
    young += (i//30) + 1
    min += (i//60) + 1

young *= 10
min *= 15
if young < min:
    print(f'Y {young}')
elif min < young:
    print(f'M {min}')
else:
    print(f'Y M {young}')