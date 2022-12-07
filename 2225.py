
n,k = [int(i) for i in input().split()]

dp = [[0] * (n+1) for _ in range(k+1)]

dp[0][0] = 1
for i in range(1,k+1):
    for j in range(0,n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp[i][j] = dp[i][j] % 1000000000
print(dp[k][n])

    