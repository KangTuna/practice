import sys

input = sys.stdin.readline

x = int(input().rstrip())

ans = [0,64]
while True:
    if sum(ans) == x:
        break
    temp = ans.pop()
    temp //= 2
    if sum(ans) + temp > x:
        ans.append(temp)
    elif sum(ans) + temp == x:
        ans.append(temp)
        break
    else:
        for _ in range(2):
            ans.append(temp)

print(len(ans) -1 )