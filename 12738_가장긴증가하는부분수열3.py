import bisect,sys

input = sys.stdin.readline

x = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
for i in dp:
    print(i,end = ' ')