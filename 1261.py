from collections import deque


n, m = map(int,input().split())
graph = [[int(i) for i in input()] for _ in range(m)]
visited = [[False] * n for _ in range(m)]
distance = [[-1] * n for _ in range(m)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):


    que = deque()
    que.append([x,y])
    distance[x][y] = 0
    while que:

        x,y = que.popleft()
        
        if x == n-1 and y == m - 1:

            return

        for i in range(4):
            nx, ny = x + dx[i], y+ dy[i]
            
          
            if nx <0  or nx >=m or ny <0 or ny>=n:
                continue
  
            if not visited[nx][ny] and graph[nx][ny] == 0:
                que.appendleft([nx,ny])
                distance[nx][ny] = distance[x][y]
                visited[nx][ny] = True
                continue
                
            
            if not visited[nx][ny]  and graph[nx][ny] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                que.append([nx,ny])
                visited[nx][ny] = True
                continue
                

bfs(0,0)
print(distance[m-1][n-1])
