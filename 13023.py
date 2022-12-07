from collections import deque
from glob import glob
import queue
N, M = map(int,input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
result = False
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(depth,graph_number):
    global result
    if depth == 4:
        result = True
        return


    for i in graph[graph_number]:
        if result == True:
            return
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(0,i)
    visited[i] = False
    if result:
        print(1)
        exit()

print(0)



