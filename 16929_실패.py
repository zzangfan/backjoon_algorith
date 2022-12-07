n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
flag = False
def dfs(y,x,before_y,before_x,color):
    if visited[y][x]:
       
       return True
    visited[y][x] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx != before_x or ny != before_y :
            if 0 <= nx < m and 0 <= ny < y:
                if graph[ny][nx] == color:
                    if dfs(ny,nx,y,x,color):
                        return True
                    
    return False
    
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if dfs(i,j,0,0,graph[i][j]):
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")

            
    


