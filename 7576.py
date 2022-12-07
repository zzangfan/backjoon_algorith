from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
res = 0
que = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i,j])

def bfs():
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n  and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[nx][ny] + 1
                que.append([nx,ny])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res,max(i))
print(res - 1)