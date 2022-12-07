from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
map = [[int(i) for i in input().split()] for _ in range(n)]

min_check = sys.maxsize
island_cnt = []
visited = [[False] * n  for _ in range(n)] 

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,island):

    island.append([x,y])
    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx >=n or ny<0 or ny>=n:
            continue

        if not visited[nx][ny] and map[nx][ny] == 1:
            visited[nx][ny] = True
            
            dfs(nx,ny,island)

    return island


def bfs(x,y,island_number):
    global min_check
    global island_cnt
    que = deque()
    
    island_check = [[-1] * n for _ in range(n)]
    for idx,i in enumerate(island_cnt):
        for x,y  in i:           
            island_check[x][y] = idx + 2
            if idx +2  == island_number:
                que.append([x,y])
    
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if nx < 0  or nx >=n  or ny <0 or ny>= n:
                continue

            if island_check[nx][ny] != island_number and island_check[nx][ny] > 0 and not visited[x][y]:
                min_check = min(min_check,island_check[x][y])
                continue

            if map[nx][ny] == 0 and island_check[nx][ny] == -1:
                island_check[nx][ny] = island_check[x][y] + 1
                
                que.append([nx,ny])



for i in range(n):
    for j in range(n):
        if not visited[i][j] and map[i][j] == 1:
            island_cnt.append(dfs(i,j,[]))


for cnt in range(2,len(island_cnt)+2):
    for i in range(n):
        for j in range(n):
            if visited[i][j] and map[i][j] == 1:
                bfs(i,j,cnt)
print(min_check)