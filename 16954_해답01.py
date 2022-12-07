from collections import deque
import sys
sys.setrecursionlimit(10**9)
#graph,wall,answer = [list(input().rstrip()) for _ in range(8)],set(),0
graph = [list(input().rstrip()) for _ in range(8)]
d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1),(0,0)]


#전체적인 보드가 움직이는걸로 생각을 했는데 그게 아니라 벽만 움직이는 거였다.

def bfs():
    
    wall = set()
    for i in range(8):
        for j in range(8):
            if graph[i][j] =='#':
                wall.add((i,j))
    
    
    visited = set()
    que = deque()
    que.append((7,0))

    while que:
        
        for _ in range(len(que)):
            x,y = que.popleft()
            if (x,y) in wall:
                continue
            if x == 0 and y == 7:
                return 1

            
            for dx, dy in d:
                nx = x + dx
                ny = y + dy

                if 0 <= nx <= 7 and  0 <= ny <= 7 and not (nx,ny) in visited and not (nx, ny) in wall:
                    visited.add((nx,ny))
                    que.append((nx,ny))
        if wall:
            visited = set()
        next_wall = set()

        for x,y in wall:
            if x < 7:
                next_wall.add((x+1,y))
        wall = next_wall
    return 0

print(bfs())