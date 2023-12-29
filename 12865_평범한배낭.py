import sys

input = sys.stdin.readline

n,k = map(int,input().rstrip().split())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    things_weight,things_value = map(int,input().rstrip().split())
    for j in range(1,k+1):
        dp[i][j] = max(dp[i][j],dp[i-1][j],dp[i][j-1])
        if j >= things_weight:
            dp[i][j] = max(dp[i][j],dp[i-1][j-things_weight]+things_value)

print(dp[n][k])