N = int(input())
A = input().split()
ans = N
num = [x*y for x in range(2,1001) for y in range(2,1001)]
num.append(1)
num = set(num)
for i in A:
    i = int(i)
    if i in num:
        ans -= 1
print(ans)
