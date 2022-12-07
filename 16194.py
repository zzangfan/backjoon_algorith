n = int(input())

p = [0] + [int(i) for i in input().split()]
dp = [False] * (n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        if dp[i] == False:
            dp[i] = dp[i-j] + p[j]
            
        else:
            dp[i] = min(dp[i],dp[i-j] + p[j])

print(dp[n])