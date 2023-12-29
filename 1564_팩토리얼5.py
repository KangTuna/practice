import sys

input = sys.stdin.readline

n = int(input().rstrip())

ans = 1
for i in range(1, n + 1):
	ans *= i
	while str(ans)[-1] == "0":
		ans //= 10
	ans %= 1000000000000

print(str(ans)[-5:])