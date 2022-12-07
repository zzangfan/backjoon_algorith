from collections import deque
N,M,K = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]

distance = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs():

    que = deque()
    que.append([0,0,0,0])
    distance[0][0][0] = 1
    time = True
    while que:
       
        x,y,z,cnt = que.popleft()
        

        if x == N - 1 and  y == M - 1:
            return distance[x][y][z]

        for i in range(4):

            nx,ny = x + dx[i],y + dy[i]

            if nx <0  or nx >= N or ny <0  or ny >=M:
                continue

            if graph[nx][ny] == 0 and distance[nx][ny][z] == 0:

                
                distance[nx][ny][z] = distance[x][y][z] + 1
                que.append([nx,ny,z,0])
                continue

            if graph[nx][ny] == 1 and z < K  and distance[nx][ny][z+1] == 0:
                
                if time:
                
                    distance[nx][ny][z+1] = distance[x][y][z] +  1 + cnt
                    
                    que.append([nx,ny,z+1,0])
                else:
                    que.append((x,y,z,1))
                
                continue

        
        time = not time

           

            
    return -1

print(bfs())


