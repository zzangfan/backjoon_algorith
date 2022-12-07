from collections import deque


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])



def bfs(start):

    que = deque()
    que.append([start,0])
    vistied = [False] * (n+1)
    vistied[start] = True
    max_index = start
    max_dis = 0

    while que:
        now_index, now_distance = que.popleft()
        if max_dis < now_distance:
            max_dis = now_distance
            max_index = now_index

        for i,d in graph[now_index]:
            if not vistied[i]:
                que.append([i,d+now_distance])
                vistied[i] = True

    return max_index, max_dis

max_index, max_dis = bfs(1)
max_index, max_dist = bfs(max_index)

print(max_dist)