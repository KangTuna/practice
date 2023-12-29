import sys

while True:
    sam = list(map(int,sys.stdin.readline().rstrip().split()))
    sam.sort()
    if sam[0] == 0:
        break
    if sam[0]**2 + sam[1]**2 == sam[2]**2:
        print("right")
    else:
        print("wrong")