
from collections import deque
def bfs(sx,sy,tx,ty):
    
    que = deque()
    que.append([sx,sy])
    graph[sx][sy] = 1
    while que:
        
        x,y = que.popleft()
        if x == tx and y == ty:
            print(graph[tx][ty] - 1)
            return
        for i in range(8):
            nx,ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
               
                que.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1
              
            

    


test_case = int(input())
dx = [-1,-1,1,1,-2,-2,2,2]
dy = [-2,2,-2,2,-1,1,-1,1]
for _ in range(test_case):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    sx,sy = map(int,input().split())
    tx,ty = map(int,input().split())
    bfs(sx,sy,tx,ty)