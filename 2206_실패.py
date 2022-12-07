from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,list(input()))) for _ in range(n)]

distance = [[-1] * m for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():

    que = deque()
    count = 1 
    que.append((0,0))
    distance[0][0] = 1

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0  or nx >=n  or ny <0  or ny >=m:
                continue
            
            if distance[nx][ny] == -1 and graph[nx][ny] == 1 and count != 0:
                count -= 1
                que.append((nx,ny))
                distance[nx][ny] = distance[x][y] + 1
                continue

            if distance[nx][ny] == -1 and graph[nx][ny] == 0:
                que.append((nx,ny))
                distance[nx][ny] = distance[x][y] + 1
                continue

bfs()

if distance[n-1][m-1] == -1:
    print(-1)
else:
    print(distance)
