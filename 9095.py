import sys
input = sys.stdin.readline
cnt = int(input())
answer = []
for _ in range(cnt):
    n = int(input())
    dp = [0] * (n+1)
    for i in range(n+1):
        if i == 1:
            dp[i] = 1 
        elif i == 2:
            dp[i] = 2
        elif  i == 3:
            dp[i] = 4
        elif i == 0:
            pass
        else:
            dp[i] = dp[i-1] + dp[i-2]+ dp[i-3]
    answer.append(dp[n])
print("\n".join(map(str,answer)))