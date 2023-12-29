import sys

input = sys.stdin.readline

data = int(input().rstrip())
arr = [x for x in range(data)]
ans = 0
def div_sum(n):
    temp = n
    div = 10000000
    while True:
        div = int(div / 10)
        temp += n//div
        n = n%div
        if div <= 1:
            break
        
    return temp
for i in arr:
    if data == div_sum(i):
        ans = i
        break

print(ans)