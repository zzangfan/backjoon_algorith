n = int(input())

a_list = [int(i) for i in input().split()]

dp = [1] * n

for i in range(n):
    for j in range(i):
        if a_list[j] < a_list[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))