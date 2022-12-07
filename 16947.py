from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(start,idx,cnt):
    global cycle
    if start == idx and cnt >= 2:
        cycle = True
        return
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            dfs(start,i,cnt+1)
        elif i == start and cnt >= 2:
            dfs(start,i,cnt)

def bfs():
    global check
    que = deque()

    for i in range(n):
        if cycle_station[i]:
            check[i] = 0
            que.append(i)

    while que:

        now = que.popleft()

        for i in graph[now]:

            if check[i] == -1:
                que.append(i)
                check[i] = check[now] + 1

    for i in check:
        print(i,end=' ')

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


check = [-1] * n
cycle_station = [False] * n


for i in range(n):
    visited = [False] * n
    cycle =False
    dfs(i,i,0)

    if cycle:
        cycle_station[i] = True

bfs()