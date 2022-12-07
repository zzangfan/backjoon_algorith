from collections import deque
n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):

    print(start,end=' ')
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
           
            
            dfs(i)
            visited[i] = True

def bfs(start):
    que = deque([start])
    visited[start] = True
    while que:
        now = que.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

dfs(start)
visited = [False] * (n+1)
print()
bfs(start)