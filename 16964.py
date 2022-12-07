import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfs(node,tree):
    global visited
    if visited[node]:return
    
    visited[node] = True
    answer.append(node)

    for i in graph[node]:
        if not visited[i]:
            dfs(i,tree)


n = int(input())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
answer = []
for _ in range(1,n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int,input().split()))
rank = [-1 for _ in range(n+1)]

for i in range(1,n+1):
    rank[order[i-1]] = i

for i in range(1,n+1):
    graph[i] = sorted(graph[i],key=lambda x: rank[x])

dfs(1,graph)

if answer == order:
    print(1)
else:
    print(0)