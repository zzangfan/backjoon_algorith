from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,list(input()))) for _ in range(n)]

distance = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():

    que = deque()
   
    que.append((0,0,0))
    distance[0][0][0] = 1

    while que:
        x,y,z = que.popleft()
        if x == n -1 and y == m -1:
            return distance[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0  or nx >=n  or ny <0  or ny >=m:
                continue

            if graph[nx][ny] == 1 and z == 0:
            
                
                distance[nx][ny][1] = distance[x][y][0] + 1
                que.append((nx,ny,1))
                continue
            
            if graph[nx][ny] == 0 and distance[nx][ny][z] == 0:
                que.append((nx,ny,z))
                distance[nx][ny][z] = distance[x][y][z] + 1
                continue
            
          
    
    return -1
            

print(bfs())

