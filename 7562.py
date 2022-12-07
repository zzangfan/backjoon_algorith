

def bfs(start_point,target_point):
    tx, ty = target_point[0],target_point[1]
    que = deque([start_point])
    while que:
        
        x,y = que.popleft()
        for i in range(8):
            nx,ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                graph[nx][ny] = min(graph[x][y] + 1,graph[nx][ny])
                que.append([nx,ny])
                if nx == tx and ny == ty:
                    return graph[tx][ty]
            

    

from collections import deque
test_case = int(input())
dx = [-1,-1,1,1,-2,-2,2,2]
dy = [-2,2,-2,2,-1,1,-1,1]
for _ in range(test_case):
    n = int(input())
    graph = [[9999999] * n for _ in range(n)]
    start_point = list(map(int,input().split()))
    graph[start_point[0]][start_point[1]] = 0
    target_point = list(map(int,input().split()))
    print(bfs(start_point,target_point))