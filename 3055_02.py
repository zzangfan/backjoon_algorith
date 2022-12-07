from collections import deque
n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]

distance = [[-1] * m for _ in range(n)]

d = ((1,0),(-1,0),(0,1),(0,-1))


def bfs(x,y,gx,gy):
    global water
    global stone
    que = deque()
    que.append((x,y))
    distance[x][y] = 0
    while que:
        
        new_water = set()
        if water:
            for x,y in water:

                for dx,dy in d:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= n  or ny <0 or ny >= m:
                        continue
                    
                    if nx == gx and ny == gy:
                        continue
                    
                    if distance[nx][ny] == -1 and (nx,ny) not in stone:
                        new_water.add((nx,ny))
                        distance[nx][ny] = - 2 
        
        water = new_water


        for _ in range(len(que)):
            x,y = que.popleft()

            if x == gx and y == gy:
                    
                return distance[gx][gy]

            for dx,dy in d:
                nx = x + dx
                ny = y + dy
                
                if nx < 0 or nx >= n  or ny <0 or ny >= m:
                    continue

                if (nx,ny) in water:
                    
                    continue

                if graph[nx][ny] == '.' and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    que.append((nx,ny))

    return 'KAKTUS'

water = set()
stone = set()
for i in range(n):
    for j in range(m):
        context = graph[i][j]
        if context == 'D':
            gx,gy = i,j
            graph[gx][gy] = '.'
        elif context == 'X':
            stone.add((i,j))
        elif context == 'S':
            x,y = i,j
            
        elif context == '*':
            water.add((i,j))

print(bfs(x,y,gx,gy))
