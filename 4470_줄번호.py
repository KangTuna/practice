import sys

input = sys.stdin.readline

T = int(input().rstrip())

data = []
for _ in range(T):
    data.append(input().rstrip())

for i in range(len(data)):
    print(f'{i+1}. {data[i]}')
    