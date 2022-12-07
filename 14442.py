from collections import deque

N,M,K = map(int,input().split())

graph = [list(map(int,input().strip())) for _ in range(N)]

distance = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(start_x,start_y):
   
    que = deque()
    que.append([start_x,start_y,0])
    distance[start_x][start_y][0] = 1

    while que:

        x,y,z = que.popleft()
        
        if x == N -1 and y == M-1:
            
            return distance[x][y][z] 

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if nx <0  or nx >= N  or ny <0 or ny>=M:
                continue

            if graph[nx][ny] == 1 and  z < K and distance[nx][ny][z+1] == 0  :

                
                distance[nx][ny][z+1] = distance[x][y][z] + 1
                que.append([nx,ny,z+1])
                continue
            
            if graph[nx][ny] == 0  and distance[nx][ny][z] == 0:
                que.append([nx,ny,z])
                distance[nx][ny][z] = distance[x][y][z] + 1
                continue


    return -1



print(bfs(0,0))

