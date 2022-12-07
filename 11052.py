n = int(input())


dp = [0] * (n+1)
a_list = [int(i) for i in input().split()]
p = [0] + a_list

for i in range(1,n+1):
    for j in range(1, i + 1):

        dp[i] = max(dp[i],dp[i-j] + p[j])
print(dp[n])
