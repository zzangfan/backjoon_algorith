import sys
input = sys.stdin.readline
n = int(input())

dp = [0] * (n+1)


for i in range(0,n+1):

    if i == 1 or i == 0:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)