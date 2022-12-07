from itertools import count
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(i,j):
    global count
    q = deque()
    q.append([i,j])
    visited[i][j] = True
    map[i][j] = count

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny <n and map[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                map[nx][ny] = count
                q.append([nx,ny])

def bfs2(cnt):
    global min_check

    distance = [[-1] * n  for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if map[i][j] == cnt:
                q.append([i,j])
                distance[i][j] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx <0  or nx >=n or ny <0 or ny >= n:
                continue
            
            if map[nx][ny] > 0 and map[nx][ny] != cnt:
                min_check = min(min_check,distance[x][y])
                return
            
            if map[nx][ny] == 0 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append([nx,ny])


n = int(input())

map = [[int(i) for i in input().split()] for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = 1
min_check= sys.maxsize

for i in range(n):
    for j in range(n):
        if not visited[i][j] and map[i][j] == 1:
            bfs(i,j)
            count += 1

for i in range(1,count):
    bfs2(i)

print(min_check)