import sys,math

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().rstrip().split())
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    sum_round = r1 + r2
    if x1 == x2 and y1 == y2:
        if sum_round == 0:
            print(1)
        elif r1 == r2:
            print(-1)
        else:
            print(0)
    elif distance > sum_round:
        print(0)
    elif distance == sum_round:
        print(1)
    else:
        if distance + min(r1,r2) < max(r1,r2):
            print(0)
        elif distance + min(r1,r2) == max(r1,r2):
            print(1)
        else:
            print(2)
    