import sys

input = sys.stdin.readline

data = [[[0 for _ in range(21)]for _ in range(21)]for _ in range(21)]

def w(a,b,c):
    global data
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    elif data[a][b][c] != 0:
        return data[a][b][c]
    elif a < b and b < c:
        data[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return data[a][b][c]
    else:
        data[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return data[a][b][c]

while True:
    a,b,c = map(int,input().rstrip().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
