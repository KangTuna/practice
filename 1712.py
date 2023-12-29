A,B,C = map(int,input().split())
count = 1
temp = C-B
if temp < 0 or temp == 0:
    count = -1
else:
    count = int(A/temp) + 1

print(count)