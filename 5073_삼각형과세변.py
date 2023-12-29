import sys

input = sys.stdin.readline
data = list(map(int,input().rstrip().split()))

while sum(data) != 0:
    check = data.pop(data.index(max(data)))
    if data.count(check) == 2:
        print("Equilateral")
    elif data.count(check) == 1:
        print("Isosceles")
    elif check >= sum(data):
        print("Invalid")
    elif data[0] == data[1]:
        print("Isosceles")
    else:
        print("Scalene")
    
    data = list(map(int,input().rstrip().split()))
