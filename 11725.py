from collections import deque


import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
parent = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(child,graph,parent):
    for i in graph[child]:
        if parent[i] == 0:
            parent[i] = child
            dfs(i,graph,parent)

dfs(1,graph,parent)

for i in range(2,n+1):
    print(parent[i])

