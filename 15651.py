n,m = [int(i) for i in input().split()]
visited = [False] * (n+1)

answer = []

def back_dfs(depth,n,m):

    if depth == m:
        print(' '.join(map(str,answer)))

    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            back_dfs(depth+1,n,m)
           
            visited[i] = False
            answer.pop()
back_dfs(0,n,m)

