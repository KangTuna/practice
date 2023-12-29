import sys

input = sys.stdin.readline

data = []
for _ in range(5):
    i = int(input().rstrip())
    if i < 40 :
        i = 40
    data.append(i)

print(sum(data)//5)