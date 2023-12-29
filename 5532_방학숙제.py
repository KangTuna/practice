import sys

input = sys.stdin.readline

L = int(input().rstrip())
A = int(input().rstrip())
B = int(input().rstrip())
C = int(input().rstrip())
D = int(input().rstrip())

Kor, Math = 0, 0 
count = 0
while True:
    if A >= C or B >= D:
        Kor += C
        Math += D
        count += 1
    if A <= Kor and B <= Math:
        print(L-count)
        break