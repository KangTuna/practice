N = int(input())
minn = 5000
data = [(x,y) for x in range(1001) for y in range(1001) if 3*x + 5*y == N]
if len(data) == 0:
    minn = -1
for i in data:
    if sum(i) < minn:
        minn = sum(i)
print(minn)