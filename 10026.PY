from collections import deque
N = int(input())
graph = []
new_graph = [[-1] * N for _ in range(N)]

for i in range(N):
    graph.append(list(input().rstrip()))
    for j in range(N):
        if graph[i][j] == 'G':
            new_graph[i][j] = 'R'
        else:
            new_graph[i][j] = graph[i][j]

d = ((1,0),(-1,0),(0,1),(0,-1))

visited = [[-1] * N for _ in range(N)]


def bfs(x,y,alpabet,group):
    global visited
    
    que = deque()
    que.append((x,y))
    visited[x][y] = group
    
    
    while que:
        x,y = que.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            
            if nx <0 or nx >= N or ny <0 or ny>=N:
                continue
            
            if graph[nx][ny] == alpabet and visited[nx][ny] == -1:
                visited[nx][ny] = group
                que.append((nx,ny))
            

group = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == -1:
            alpabet = graph[i][j]
            group += 1
            bfs(i,j,alpabet,group)
print(group,end=' ')

group = 0
graph = new_graph
visited = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == -1:
            alpabet = graph[i][j]
            group += 1
            bfs(i,j,alpabet,group)


print(group)

    
            

        