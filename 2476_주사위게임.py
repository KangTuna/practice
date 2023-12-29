import sys

input = sys.stdin.readline

n = int(input().rstrip())

price = []
for _ in range(n):
    data = list(map(int,input().rstrip().split()))
    check = data.pop()
    if data.count(check) == 2:
        price.append(10000 + (1000 * check))
    elif data.count(check) == 1:
        price.append(1000 + (100 * check))
    elif data[0] == data[1]:
        price.append(1000 + (100 * data[0]))
    else:
        data.append(check)
        price.append(100 * max(data))

print(max(price))
        