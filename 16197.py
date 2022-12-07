from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
ball_loc = []
min_value = sys.maxsize
visited = [[False] * m for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
distance_02 = [[-1] * m for _ in range(n)]

for i in range(n):
    graph[i] = (list(input().rstrip()))

def bfs_check(x,y):
    global ball_loc
    que = deque()
    que.append([x,y])
    visited[x][y] = True
    while que:
        
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if nx <0 or nx >=n or ny <0 or ny>=m:
                continue

            if not visited[nx][ny] and graph[nx][ny] =='o':
                ball_loc.append([nx,ny])
                return True

            if not visited[nx][ny] and graph[nx][ny] =='.':
                que.append([nx,ny])
                visited[nx][ny] = True
    
    return False

def bfs(x,y,x_2,y_2):
    global min_value
    que = deque()
    que.append([(x,y),(x_2,y_2)])
    distance[x][y] = 0
    distance[x_2][y_2] = 0

    while que:
        (x,y),(x_2,y_2) = que.popleft()
        for i in range(4):
            nx ,ny = x + dx[i], y + dy[i]
            nx_2, ny_2 = x_2 +dx[i], y +dy[i]
            temp = []
            if (nx<0 or nx>=n or ny<0 or ny>=m) != (nx_2<0 or nx_2 >=n or ny_2 <0 or ny_2 >=m):
                
                if (nx<0 or nx>=n or ny<0 or ny>=m):
                    min_value = min(min_value,distance[x][y])
                    continue
                if (nx_2<0 or nx_2 >=n or ny_2 <0 or ny_2 >=m):
                    min_value = min(min_value,distance_02[x][y])
                    continue
            if (nx<0 or nx>=n or ny<0 or ny>=m):
                continue

            if (nx_2<0 or nx_2 >=n or ny_2 <0 or ny_2 >=m):
                continue
            
            if distance[nx][ny] == -1 and graph[nx][ny] == '.':
                distance[nx][ny] = distance[x][y] + 1
                temp.append((nx,ny))
            if distance_02[nx_2][ny_2] == -1 and graph[nx_2][ny_2] =='.':
                
                distance_02[nx_2][ny_2] = distance[nx][ny] + 1
                temp.append((nx_2,ny_2))
            if distance[nx][ny] == -1 and graph[nx][ny] == '#':
                distance[nx][ny] = -2
                
            if distance_02[nx_2][ny_2] == -1 and graph[nx_2][ny_2] =='#':
                 distance_02[nx_2][ny_2] == -2
                 

            
            que.append(temp)

def check_block():
    for i in range(n):
        for j in range(m):
            if graph[i][j] =='o':
                ball_loc.append([i,j])
                if bfs_check(i,j):
                   return 
                elif not bfs_check(i,j):
                    print(-1)
                    exit()
check_block()
(x,y),(x_2,y_2) = ball_loc
bfs(x,y,x_2,y_2)
