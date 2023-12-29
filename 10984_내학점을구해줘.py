import sys

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    m = int(input().rstrip())
    temp = 0
    total = 0
    for i in range(m):
        a,b = input().rstrip().split()
        a,b = int(a),float(b)
        temp += a * b
        total += a
    print(f'{total} {temp/total:.1f}')