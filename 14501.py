n = int(input())
delay_day = [[int(i) for i in input().split() ]for _ in range(n)]

max_value = -99999
answer = []
def back_dfs(depth):
    global max_value
    if depth <= n:
        
        max_value = max(max_value,sum(answer))
        

    for i in range(depth,n):

        T,P = delay_day[i]
        answer.append(P)
        back_dfs(i+T)
        answer.pop()
        
back_dfs(0)
print(max_value)




xdg