n = int(input())

a_list = [int(i) for i in input().split()]
dp = [a_list[0]] + [0] * (n)

negative_check = []
for i in a_list:
    if i<0:
        negative_check.append(True)
    else:
        negative_check.append(False)

if sum(negative_check) == n:
    print(max(a_list))
else:

    for i in range(1,n):

        dp[i] = max(dp[i],dp[i-1]+a_list[i])


    print(max(dp))