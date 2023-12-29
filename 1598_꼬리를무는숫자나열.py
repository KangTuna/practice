import sys

input = sys.stdin.readline

a,b = map(int,input().rstrip().split())

if a % 4 == 0:
    row_a = (a//4) - 1
    col_a = 4
else:
    row_a = a//4
    col_a = a%4

if b % 4 == 0:
    row_b = (b//4) - 1
    col_b = 4
else:
    row_b = b//4
    col_b = b%4


row = abs(row_a - row_b)
col = abs(col_a - col_b)

print(row+col)