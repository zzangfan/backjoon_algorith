n,m = map(int,input().split())
visited = [False] * n

answer = []
def back_dfs():
    if len(answer) == m:
        print(' '.join(map(str,answer)))
        return
    for i in range(1,n + 1):
        
            answer.append(i)
            back_dfs()
            answer.pop()


back_dfs()