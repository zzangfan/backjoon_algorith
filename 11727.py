import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)


for i in range(n+1):
    if i ==0  or  i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = dp[i-1] + 2* dp[i-2]
print(dp[n]%10007)
