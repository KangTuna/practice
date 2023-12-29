import sys

input = sys.stdin.readline

n = int(input().rstrip())
count = 0
board = [0 for _ in range(n)]

def possible(cdx):
    for i in range(cdx):
        if board[cdx] == board[i] or cdx-i == abs(board[cdx] - board[i]):
            return 0
    return 1

def nqueen(cdx):
    global count
    if cdx == n:
        count += 1
        return
    
    for i in range(n):
        board[cdx] = i
        if possible(cdx):
            nqueen(cdx+1)

nqueen(0)
print(count)

# import sys

# input = sys.stdin.readline

# n = int(input().rstrip())

# data = {1 : 1,
#         2 : 0,
#         3 : 0,
#         4 : 2,
#         5 : 10,
#         6 : 4,
#         7 : 40,
#         8 : 92,
#         9 : 352,
#         10 : 724,
#         11 : 2680,
#         12 : 14200,
#         13 : 73712,
#         14 : 365596}

# print(data[n])