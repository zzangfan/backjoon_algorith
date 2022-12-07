from collections import deque
import sys
sys.setrecursionlimit(100000)


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


def dfs(x,y):

    for a,b in graph[x]:
        if distance[a] == -1:
            distance[a] = y + b
            dfs(a,y+b)

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1,0)


start = distance.index(max(distance))

distance = [-1] * (n + 1)
distance[1] = 0
dfs(start,0)

print(max(distance))