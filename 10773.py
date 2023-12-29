import sys

K = int(sys.stdin.readline().rstrip())
data = []
for i in range(K):
    Z = int(sys.stdin.readline().rstrip())
    if Z == 0:
        data.pop()
    else:
        data.append(Z)

print(sum(data))